# To use this code install julia 1.0 (https://julialang.org/downloads/)
# (available for linux/osx/windows)

# For the verification code we do not need the solver, but for solving the sdps
# we need sdpa_gmp (http://sdpa.sourceforge.net/). For getting high precision output 
# from sdpa_gmp we need to use a patched version, which is available on 
# http://www.daviddelaat.nl/sdpa-gmp-7.1.3.tar.gz 
# Make sure that the sdpa_gmp binary is callable (add it to PATH)

# To install Nemo, AbstractAlgebra, and Optim run julia and type
# julia> Pkg.add("Nemo")
# julia> Pkg.add("Optim")
# (This code has been tested with AbstractAlgebra 0.1.3 and Nemo 0.10.1)

# To use this code run julia in this folder and type
# julia> push!(LOAD_PATH, pwd())
# julia> using ZetaBounds

# For the verification code run
# julia> rverify(:Z, 40)
# julia> rverify(:tildeZ, 40)
# julia> rverify(:Z1, 40)
# julia> rverify(:L, 40)
# julia> gverify(:P, 40)
# julia> gverify(:tildeP, 40)

# For setting up and solving the sdps run, e.g.,
# julia> rsolve(:Z, 40)

module ZetaBounds

using Nemo, AbstractAlgebra, LinearAlgebra, Optim, Printf

export r, roptimize, rstore, rverify, rvalues, g, gfindlambda, goptimize, gstore, gverify

import Base: zero, inv, one, +, -, *, /, //, ^, length, show, getindex, iszero, ==, copy, isequal
import LinearAlgebra.norm

#################################
### SDP specification library ###
#################################

# For simplicity we implement AffineExpression as a ring and give an error when an operation is not possible.
struct Entry
    blockname
    i
    j
    Entry(name, i, j) = new(name, min(i, j), max(i, j))
end

function ==(a::Entry, b::Entry)
    a.blockname == b.blockname && a.i == b.i && a.j == b.j
end

show(io::IO, entry::Entry) = print(io, entry.blockname, '[', entry.i, ',', entry.j, ']')

struct AffineExpressionRing{T} <: AbstractAlgebra.Ring
    base_ring
end

AffineExpressionRing(ring::T) where T<:AbstractAlgebra.Ring = AffineExpressionRing{elem_type(ring)}(ring)

mutable struct AffineExpression{T} <: AbstractAlgebra.RingElem where T
    parent::AbstractAlgebra.Ring
    variables::Vector{Entry}
    coefficients::Vector{T}
    constant::T
    function AffineExpression{T}(variables, coefficients, constant) where T
        @assert length(variables) == length(coefficients)    
        nonzerolist = [i for i in eachindex(coefficients) if !iszero(coefficients[i])]
        new(AffineExpressionRing(parent(constant)), variables[nonzerolist], coefficients[nonzerolist], constant)
    end
end

function AbstractAlgebra.parent_type(::Type{AffineExpression{T}}) where T
    AffineExpressionRing{T}
end

function AbstractAlgebra.elem_type(::Type{AffineExpressionRing{T}}) where T
    AffineExpression{T}
end

function AbstractAlgebra.base_ring(R::AffineExpressionRing{T}) where T
    R.base_ring
end

AbstractAlgebra.parent(ae::AffineExpression) = ae.parent

AbstractAlgebra.isdomain_type(::Type{AffineExpression}) = false

isexact_type(::Type{AffineExpression{T}}) where T = isexact_type(T)

Base.hash(f::AffineExpression{T}, h::UInt) where T = hash(f.variables) + hash(f.coefficients) + hash(f.constant)

function (R::AffineExpressionRing{T})() where T
    AffineExpression(Entry[], T[], zero(base_ring(R)))
end

function (R::AffineExpressionRing{T})(a::RingElement) where T
    AffineExpression(Entry[], T[], base_ring(R)(a))
end

function (R::AffineExpressionRing{T})(a::AffineExpression{T}) where T
    a
end

function (R::AffineExpressionRing{T})(a::T) where T
    AffineExpression(Entry[], T[], base_ring(R)(a))
end

function zero(R::AffineExpressionRing{T}) where T
    AffineExpression(Entry[], T[], zero(base_ring(R)))
end

function one(R::AffineExpressionRing{T}) where T
    AffineExpression(Entry[], T[], one(base_ring(R)))
end

function zero(R::AffineExpression{T}) where T
    AffineExpression(Entry[], T[], zero(base_ring(parent(R))))
end

function one(R::AffineExpression{T}) where T
    AffineExpression(Entry[], T[], one(base_ring(parent(R))))
end

function iszero(a::AffineExpression)
    all(iszero, a.coefficients) && iszero(a.constant)
end

function isone(a::AffineExpression{T}) where T
    all(iszero, a.coefficients) && a.constant == one(T)
end

canonical_unit(f::AffineExpression) = one(parent(f))

function entry(T, name, i, j)
    AffineExpression([Entry(name, i, j)], [one(T)], zero(T))
end

getindex(ae::AffineExpression, i) = (ae.coefficients[i], ae.variables[i])

function show(io::IO, ae::AffineExpression{T}) where T
    for k = 1:length(ae)-1
        coeff, entry = ae[k]
        if coeff != one(coeff)
            print(io, coeff, '*')
        end
        print(entry, " + ")
    end
    if length(ae) >= 1
        coeff, entry = ae[length(ae)]
        if coeff != one(coeff)
            print(io, coeff, '*')
        end
        print(io, entry)
    end
    if ae.constant > 0
        print(io, " + ", ae.constant)
    elseif ae.constant < 0
        print(io, " - ", abs(ae.constant))
    end
end

function AffineExpression(variables::Vector{Entry}, coefficients::Vector{T}, constant::T) where T
    AffineExpression{T}(variables, coefficients, constant)
end

function length(a::AffineExpression)
    @assert length(a.variables) == length(a.coefficients)
    length(a.variables)
end

*(a::T, b::Vector{T}) where {T<:Number} = [a*x for x in b]
*(a::T, b::Vector{T}) where {T<:RingElem} = [a*x for x in b]
/(a::Vector{T}, b::T) where {T<:Number} = [x/a for x in b]
/(a::Vector{T}, b::T) where {T<:RingElem} = [x/a for x in b]

//(a::BigFloat, b::BigFloat) = a/b

AbstractAlgebra.promote_rule(::Type{AffineExpression{T}}, ::Type{AffineExpression{T}}) where T <: RingElement = AffineExpression{T}

function AbstractAlgebra.promote_rule(::Type{AffineExpression{T}}, ::Type{U}) where {T <: RingElement, U <: RingElement}
   AbstractAlgebra.promote_rule(T, U) == T ? AffineExpression{T} : Union{}
end

function Base.iterate(a::AffineExpression, state=1)
    if state > length(a.coefficients) 
        nothing
    else
        ((a.variables[state], a.coefficients[state]), state+1)
    end
end

function //(a::AffineExpression{T}, s::S) where {S,T}
    R = promote_type(S, T)
    AffineExpression{R}(a.variables, a.coefficients/s, a.constant/s)
end

function /(a::AffineExpression{T}, s::S) where {S,T}
    R = promote_type(S, T)
    AffineExpression{R}(a.variables, a.coefficients/s, a.constant/s)
end

function ^(a::AffineExpression{T}, n::Integer) where {T}
    if n == 0
        one(a)
    elseif n == 1
        a
    else
        if length(a) == 0
            AffineExpression(Entry[], T[], a.constant^n)
        else
            error("Impossible power of affine expressions")
        end
    end
end

AbstractAlgebra.isnegative(::AffineExpression) = false

function norm(a::AffineExpression)
    sqrt(sum(a.coefficients.^2) + a.constant^2)
end

function +(a::AffineExpression{T}, b::AffineExpression{T}) where {T}
    if a.variables == b.variables
        AffineExpression{T}(a.variables, a.coefficients + b.coefficients, a.constant + b.constant)
    else
        variables = copy(a.variables)
        coefficients = copy(a.coefficients)
        for i = 1:length(b.variables)
            j = findfirst(isequal(b.variables[i]), variables)
            if j == nothing
                push!(variables, b.variables[i])
                push!(coefficients, b.coefficients[i])
            else
                coefficients[j] += b.coefficients[i]
            end
        end
        AffineExpression{T}(variables, coefficients, a.constant+b.constant)
    end
end

function +(a::AffineExpression{S}, b::AffineExpression{T}) where {S,T}
    R = promote_type(S, T)
    variables = copy(a.variables)
    coefficients = convert(Vector{R}, copy(a.coefficients))
    for i = 1:length(b.variables)
        j = findfirst(isequal(b.variables[i]), variables)
        if j == nothing
            push!(variables, b.variables[i])
            push!(coefficients, convert(R, b.coefficients[i]))
        else
            coefficients[j] += convert(R, b.coefficients[i])
        end
    end
    AffineExpression{R}(variables, coefficients, a.constant+b.constant)
end

function -(a::AffineExpression{T}) where T
    AffineExpression(a.variables, -a.coefficients, -a.constant)
end

function -(a::AffineExpression{T}, b::AffineExpression{T}) where {T}
    if a.variables == b.variables
        AffineExpression{T}(a.variables, a.coefficients - b.coefficients, a.constant - b.constant)
    else
        variables = copy(a.variables)
        coefficients = copy(a.coefficients)
        for i = 1:length(b.variables)
            j = findfirst(isequal(b.variables[i]), variables)
            if j == nothing
                push!(variables, b.variables[i])
                push!(coefficients, -b.coefficients[i])
            else
                coefficients[j] -= b.coefficients[i]
            end
        end
        AffineExpression{T}(variables, coefficients, a.constant-b.constant)
    end
end

function -(a::AffineExpression{S}, b::AffineExpression{T}) where {S,T}
    R = promote_type(S, T)
    variables = copy(a.variables)
    coefficients = convert(Vector{R}, copy(a.coefficients))
    for i = 1:length(b.variables)
        j = findfirst(isequal(b.variables[i]), variables)
        if j == nothing
            push!(variables, b.variables[i])
            push!(coefficients, -convert(R, b.coefficients[i]))
        else
            coefficients[j] -= convert(R, b.coefficients[i])
        end
    end
    AffineExpression{R}(variables, coefficients, a.constant-b.constant)
end

function *(a::AffineExpression{T}, b::AffineExpression{T}) where T
    if length(a) == 0
        AffineExpression{T}(b.variables, a.constant * b.coefficients, a.constant * b.constant)
    elseif length(b) == 0
        AffineExpression{T}(a.variables, b.constant * a.coefficients, a.constant * b.constant)
    else
        error("Trying to multiply two nonconstant affine expressions")
    end
end

function /(a::AffineExpression{T}, b::AffineExpression{T}) where T
    if length(b) == 0
        AffineExpression{T}(a.variables, a.coefficients ./ b.constant, a.constant / b.constant)
    else
        error("Trying impossible division of affine expressions")
    end
end

function inv(a::AffineExpression{T}) where T
    if length(a) == 0
        AffineExpression{T}(a.variables, a.coefficients, inv(a.constant))
    else
        error("Trying impossible inversion")
    end
end

function copy(a::AffineExpression)
    AffineExpression(copy(a.variables), copy(a.coefficients), a.constant)
end

function ==(a::AffineExpression{T}, b::AffineExpression{T}) where T
    a.parent == b.parent && a.constant == b.constant && a.variables == b.variables && a.coefficients == b.coefficients
end

function AbstractAlgebra.mul!(a::AffineExpression{T}, b::AffineExpression{T}, c::AffineExpression{T}) where T
    a = b*c
end

function AbstractAlgebra.addeq!(a::AffineExpression{T}, b::AffineExpression{T}) where T
    if a.variables == b.variables
        a.coefficients += b.coefficients
        a.constant += b.constant
        a
    else
        a = a+b
    end
end

function AbstractAlgebra.zero!(a::AffineExpression{T}) where T
    a.variables = Entry[]
    a.coefficients = T[]
    a.constant = zero(T)
    a
end

function AbstractAlgebra.add!(a::AffineExpression{T}, b::AffineExpression{T}, c::AffineExpression{T}) where T
    if a.variables == b.variables == c.variables
        a.coefficients = b.coefficients
        a.coefficients += c.coefficients
        a.constant = b.constant + c.constant
        a
    else
        a = b+c
    end
end

function AbstractAlgebra.divexact(a::AffineExpression{T}, b::AffineExpression{T}) where T
    if length(b.variables) == 0 && !iszero(b.constant)
        AffineExpression(a.variables, [x//b.constant for x in a.coefficients], a.constant//b.constant)
    else
        error("Trying to divide by nonconstant AffineExpression")
    end
end

function AbstractAlgebra.needs_parentheses(::AffineExpression)
    true
end

function AbstractAlgebra.isone(a::AffineExpression)
    length(a.variables) == 0 && a.constant == 1
end

abstract type Objective{T}; end

struct Minimize{T} <: Objective{T}
    obj::AffineExpression{T}
end

struct Maximize{T} <: Objective{T}
    obj::AffineExpression{T}
end

function generatemapping(objective::Union{T,AffineExpression{T}}, linearconstraints) where T 
    namemap = Dict{Any, Tuple{Int, Dict{Any, Int}}}()
    nextblockindex = 1
    nextentryindices = Dict{Any, Int}()
    l = typeof(objective) != T ? [objective, linearconstraints...] : linearconstraints
    for affexpr in l
        for entry in affexpr.variables
            if haskey(namemap, entry.blockname)
                blockindex, idxmapping = namemap[entry.blockname] 
            else
                blockindex = nextblockindex
                nextblockindex += 1
                idxmapping = Dict{Any, Int}()  
            end
            if !haskey(idxmapping, entry.i)
                idx = get(nextentryindices, entry.blockname, 1)
                idxmapping[entry.i] = idx
                nextentryindices[entry.blockname] = idx + 1
            end
            if !haskey(idxmapping, entry.j)
                idx = get(nextentryindices, entry.blockname, 1)
                idxmapping[entry.j] = idx
                nextentryindices[entry.blockname] = idx + 1
            end
            namemap[entry.blockname] = (blockindex, idxmapping)
        end
    end
    namemap
end

struct SparseSDP{T}
    maximize::Bool
    namemap::Dict{Any, Tuple{Int, Dict{Any, Int}}}
    objective::Union{T,AffineExpression{T}}
    linearconstraints::Vector{AffineExpression{T}}
    function SparseSDP{T}(maximize, objective, linearconstraints) where T
        nm = generatemapping(objective, linearconstraints)
        new(maximize, nm, objective, linearconstraints)
    end
end

function SparseSDP(objective::Objective{T}, constraints::AffineExpression{T}...) where T
    SparseSDP{T}(typeof(objective) == Maximize{T}, objective.obj, collect(constraints))
end

function SparseSDP(constraints::AffineExpression{T}...) where T
    SparseSDP{T}(true, parent(constraints[1])(0), collect(constraints))
end

function psdvariable(R::AffineExpressionRing{T}, n::Int, blockname=rand(Int)) where T
    [AffineExpression([Entry(blockname, i, j)], [one(base_ring(R))], zero(base_ring(R))) for i=1:n, j=1:n]
end

function blocksizes(sdp::SparseSDP)
    nm = sdp.namemap
    d = Dict{Int,Int}()
    for (i, dict) in values(nm)
        d[i] = length(dict)
    end
    [d[i] for i = 1:length(d)]    
end

function sdpasparse(sdp::SparseSDP{T}, io::IO=stdout, R=BigFloat) where T
    nm = sdp.namemap

    println(io, length(sdp.linearconstraints))
    println(io, length(nm))
    
    d = Dict{Int,Int}()
    for (i, dict) in values(nm)
        d[i] = length(dict)
    end
    for k = 1:length(d)
        print(io, d[k], ' ')
    end
    println(io)
    
    for constraint in sdp.linearconstraints[1:end-1]
        print(io, -R(constraint.constant), ' ')
    end
    if length(sdp.linearconstraints) > 0
        println(io, -R(sdp.linearconstraints[end].constant))
    end
    
    for i = 0:length(sdp.linearconstraints)
        ac = i == 0 ? sdp.objective : sdp.linearconstraints[i]
        if i == 0 && typeof(sdp.objective) == T
            continue
        end
        for (entry, value) in ac
            v = value
            if !sdp.maximize && i==0 
                v = -v
            end
            if entry.i != entry.j
                v = v // typeof(v)(2)
            end
            a = nm[entry.blockname][2][entry.i]
            b = nm[entry.blockname][2][entry.j]
            if !iszero(v)
                println(io, i, ' ', nm[entry.blockname][1], ' ', min(a,b), ' ', max(a,b), ' ', R(v))
            end
        end
    end
end

struct SparseSDPSolution
    namemap::Dict{Any, Tuple{Int, Dict{Any, Int}}}
    primalobj
    dualobj
    primalmatrices::Vector{Matrix}
    dualvector::Vector
    dualmatrices::Vector{Matrix}
end

function +(a::SparseSDPSolution, b::SparseSDPSolution)
    @assert a.namemap == b.namemap
    SparseSDPSolution(a.namemap, a.primalobj + b.primalobj, 
                      a.dualobj + b.dualobj, a.primalmatrices .+ b.primalmatrices, 
                      a.dualvector + b.dualvector, a.dualmatrices .+ b.dualmatrices)
end

function /(a::SparseSDPSolution, c)
    SparseSDPSolution(a.namemap, a.primalobj/c, 
                      a.dualobj/c, a.primalmatrices./c, 
                      a.dualvector/c, a.dualmatrices./c)
end

primalobj(sol::SparseSDPSolution) = sol.primalobj

dualobj(sol::SparseSDPSolution) = sol.dualobj

primalmatrices(sol::SparseSDPSolution) = sol.primalmatrices

function getindex(sol::SparseSDPSolution, entry::Entry)
    bi = sol.namemap[entry.blockname][1]
    i = sol.namemap[entry.blockname][2][entry.i]
    j = sol.namemap[entry.blockname][2][entry.j]
    sol.primalmatrices[bi][i, j]
end

function getindex(sol::SparseSDPSolution, ae::AffineExpression)
    sum(coeff * sol[entry] for (entry, coeff) in ae) + ae.constant
end

function getindex(sol::SparseSDPSolution, m::AbstractArray{AffineExpression{R}}) where {R}
    A = Array{R}(undef, size(m)...)
    for i = 1:length(m)
        A[i] = sol[m[i]]
    end
    A
end

function getindex(sol::SparseSDPSolution, m::AbstractArray{AbstractArray{AffineExpression{R}}}) where {R}
    B = Array{Array{S}}(undef, size(m)...)
    for i = 1:length(m)
        B[i] = Array{S}(undef, size(m[i])...)
        for j = 1:length(m[i])
            B[i][j] = sol[m[i][j]]
        end
    end
    B
end

function getindex(sol::SparseSDPSolution, m::PolyElem{AffineExpression{S}}) where {S}
    R, x = PolynomialRing(parent(m), string(var(parent(m))))
    p = zero(R)
    for i = 0:degree(m)
        p += sol[m.coeffs[i+1]] * x^i
    end
    p
end

abstract type AbstractSolver end

abstract type AbstractSDPA <: AbstractSolver end

struct SDPA <: AbstractSDPA
    executable::String
    verbose::Bool
    T
end

SDPA(; executable::String="sdpa", 
       verbose::Bool=true) = SDPA(executable, verbose, Float64)

struct SDPAQD <: AbstractSDPA
    executable::String
    verbose::Bool
    T
end

SDPAQD(; executable::String="sdpa_qd", 
         verbose::Bool=true) = SDPAQD(executable, verbose, BigFloat)

struct SDPAGMP <: AbstractSDPA
    executable::String
    verbose::Bool
    T
    maxiteration::Int
    epsilonstar
    lambdastar
    omegastar
    lowerbound
    upperbound
    betastar
    betabar
    gammastar
    epsilondash
    precision::Int
end

SDPAGMP(p::Integer=0; eps="1e-30",
        executable::String="sdpa_gmp", 
        verbose::Bool=true,
        maxiteration=10000,
        epsilonstar=eps,
        lambdastar="1e4",
        omegastar="2.0",
        lowerbound="-1e5",
        upperbound="1e5",
        betastar=["0.1","0.01","0.2"][1+p],
        betabar= ["0.3","0.02","0.4"][1+p],
        gammastar=["0.9","0.98","0.5"][1+p],
        epsilondash=eps,
        precision=[200,100,300][1+p]) = 
               SDPAGMP(executable, verbose, BigFloat, maxiteration,
                       epsilonstar, lambdastar, omegastar, lowerbound,
                       upperbound, betastar, betabar, gammastar,
                       epsilondash, precision)

# Ugly function for solving with sdpa solvers
function solvesdp(sdp::SparseSDP, solver::AbstractSDPA, inputfile = "", outputfile = ""; removefiles=true)
    T = solver.T
    function commasplit(s)
        l = []
        c = 0
        prev = 1
        for i = 1:length(s)
            if s[i] == '{'
                c+=1
            elseif s[i] == '}'
                c-=1
            elseif s[i] == ',' && c == 0
                push!(l, s[prev:i-1])
                prev = i+1
            end
        end
        push!(l, s[prev:end])
        l            
    end

    function parselist(x)
        if x[1] == '{'
            [parselist(w) for w in commasplit(x[2:end-1])]
        else
            parse(BigFloat, x)
        end
    end

    function ff(x, s)
        for i = 1:length(x)-length(s)+1
            if x[i:i+length(s)-1] == s
                return i
            end
        end
        0
    end

    function stringnormalize(x)
        r = String([c for c in x if c != ' ' && c != '\n'])
        i = ff(r, "}{")
        while i != 0 
            r = r[1:i] * "," * r[i+1:end]
            i = ff(r, "}{")
        end
        r
    end 

    if inputfile == ""
        inputfile, io = mktemp()
        sdpasparse(sdp, io, T)
        close(io)
    end
    if outputfile == ""
        outputfile = tempname()
    end
    pobj=dobj =zero(T)
    status = ""
    paramfile , paramio = mktemp()
    println(paramio, solver.maxiteration, " unsigned int maxIteration;")
    println(paramio, solver.epsilonstar, " double 0.0 < epsilonStar;")
    println(paramio, solver.lambdastar, " double 0.0 < lambdaStar;")
    println(paramio, solver.omegastar, " double 1.0 < omegaStar;")
    println(paramio, solver.lowerbound, " double lowerBound;")
    println(paramio, solver.upperbound, " double upperBound;")
    println(paramio, solver.betastar, " double 0.0 <= betaStar <  1.0;")
    println(paramio, solver.betabar, " double 0.0 <= betaBar  <  1.0, betaStar <= betaBar;")
    println(paramio, solver.gammastar, " double 0.0 < gammaStar  <  1.0;")
    println(paramio, solver.epsilondash, " double 0.0 < epsilonDash;")
    println(paramio, solver.precision, " precision; ")
    flush(paramio)
    close(paramio)
    open(`$(solver.executable) -ds $inputfile -o $outputfile -p $paramfile`) do io
        for l in eachline(io)
            solver.verbose && println(l)
            if startswith(l, "objValPrimal = ")
                pobj = parse(T, split(l, " = ")[2])
            end
            if startswith(l, "objValDual   = ")
                dobj = parse(T, split(l, " = ")[2])
            end
            if startswith(l, "phase.value = ")
                status = strip(split(l, " = ")[2])
            end
        end
    end
    
    xstring = ""
    Xstring = ""
    Ystring = ""
    open(outputfile) do io
        xbool = Xbool = Ybool = false
        for l in eachline(io)
            if startswith(l, "xVec =")
                xbool = true
            elseif startswith(l, "xMat =")
                xbool = false
                Xbool = true
            elseif startswith(l, "yMat =")
                Xbool = false
                Ybool = true
            elseif startswith(l, "    main loop time")
                Ybool = false
            elseif xbool
                xstring *= strip(l)
            elseif Xbool
                a = strip(l)
                Xstring *= a
            elseif Ybool 
                a = strip(l)
                Ystring *= a
            end
        end    
    end
    
    y = parselist(stringnormalize(xstring))

    X = parselist(stringnormalize(Xstring))
    
    finalZ = Matrix{T}[]
    for m in X
        n = length(m)
        A = Array{T}(undef, n, n)
        if typeof(m[1]) <: Vector
            for i = 1:n, j = 1:n
                A[i, j] = m[i][j]
            end
        else
            for i= 1:n
                A[i, i] = m[i]
            end
        end 
        push!(finalZ, A)
    end
    
    finalY = Matrix{T}[]
    Y = parselist(stringnormalize(Ystring))
    for m in Y
        n = length(m)
        A = Array{T}(undef, n, n)
        if typeof(m[1]) <: Vector
            for i = 1:n, j = 1:n
                A[i, j] = m[i][j]
            end
        else
            for i= 1:n
                A[i, i] = m[i]
            end
        end 
        push!(finalY, A)
    end
    
    if removefiles
        rm(inputfile)
        rm(outputfile)
        rm(paramfile)
    end
    
    v = BigFloat(typeof(sdp.objective) <: AffineExpression ? sdp.objective.constant : sdp.objective)
    status == "pdOPT", SparseSDPSolution(sdp.namemap, (sdp.maximize ? pobj : -pobj) + v, sdp.maximize ? dobj : -dobj, finalY, y, finalZ)
end

function quadform(M, v)
    sum((i==j ? 1 : 2)*v[i]*v[j]*M[i,j] for i=1:length(v) for j=i:length(v))
end

function monomials(vars, degree)
    degree == 0 && return [one(vars[1])]
    d = [digits(k, base=degree+1, pad=length(vars)) for k=0:(degree+1)^length(vars)-1]
    [prod(vars[k]^exps[k] for k=1:length(vars)) for exps in d if sum(exps) <= degree]
end

function sos(vector; name=rand(Int))
    M = psdvariable(base_ring(vector[1]), length(vector), name)
    v = 0
    for i = 1:length(vector), j = i:length(vector)
        v += (i==j ? 1 : 2) * M[i, j] * vector[i] * vector[j]
    end
    v
end

function sos(vars, totaldegree::Integer; name=rand(Int))
    @assert length(vars) >= 1
    m = monomials(vars, totaldegree)
    M = psdvariable(base_ring(vars[1]), length(m), name)
    v = 0
    for i = 1:length(m), j = i:length(m)
        v += (i==j ? 1 : 2) * M[i, j] * m[i] * m[j]
    end
    v
end

function mycoeff(p, exp)
    i = findfirst(isequal(exp), p.exps)
    i == nothing ? zero(p) : p.coeffs[i]
end

function coeffs_in_basis(p::PolyElem{T}, basis) where T
    A = [i <= degree(basis[j])+1 ? coeff(basis[j], i-1) : zero(base_ring(p)) for i in eachindex(basis), j in eachindex(basis)]
    x = Vector{T}(undef, length(basis))
    for i = length(basis):-1:1
        rhs = i <= degree(p)+1 ? coeff(p, i-1) : zero(base_ring(p))
        x[i] = rhs 
        for j=i+1:size(A,2)
            x[i] -= A[i,j]*x[j]
        end
        x[i] /= A[i,i]
    end
    r = vcat([coeff(p, i) for i=0:degree(p)], [zero(base_ring(p)) for _ = length([coeff(p, i) for i=0:degree(p)])+1:length(basis)])
    v = A*x - r
    x
end

############################################
### Missing functions in Julia libraries ###
############################################

Base.length(::Nemo.arb) = 1
Base.iterate(a::Nemo.arb, state=0) = state == 0 ? (a, 1) : nothing

function Base.BigFloat(a::Nemo.fmpq)
    big(a.num) / a.den
end

function Base.BigFloat(a::Nemo.arb)
    s = split(string(a))[1]
    if length(s) >= 2 && s[1:2] == "[+"
        return BigFloat(0)
    end
    parse(BigFloat, s[1] == '[' ? s[2:end] : s)
end

function LinearAlgebra.dot(p::PolyElem{T}, q::PolyElem{T}) where T 
    p * q
end

function AbstractAlgebra.subst(p::MPolyElem, v::Vector)
    @assert length(vars(parent(p))) == length(v) 
    r = zero(p)
    for i = 1:length(p)
        r += p.coeffs[i] * prod(v[k]^p.exps[k, i] for k = 1:length(vars(parent(p))))
    end
    r
end

function coeffs(p::MPolyElem)
    p.coeffs[1:length(p)]
end

function mycholesky(x::arb_mat)
    y = zero_matrix(base_ring(x), size(x, 1), size(x, 2))
    status = ccall((:arb_mat_cho, :libarb), Cint, (Ref{arb_mat}, Ref{arb_mat}, Int), y, x, prec(base_ring(x)))
    if status == 0
        error("not psd?")
    else
        y
    end
end

function myuppergamma(k, x::arb)
    k = parent(x)(k)
    r = parent(x)(0)
    ccall((:arb_hypgeom_gamma_upper, :libarb), Cint, (Ref{arb}, Ref{arb}, Ref{arb}, Int, Int), r, k, x, 0, prec(parent(x)))
    r
end

Base.isless(a::arb, b::arb) = a<b

LinearAlgebra.dot(a::arb, b::arb) = a*b

(Base.Rational{BigInt})(a::Nemo.arb) = Rational{BigInt}(BigFloat(a))

########################
### Helper functions ###
########################

# The kth Laguerre polynomial with parameter alpha evaluated at x.
function laguerre(k::Integer, alpha, x; prev=nothing, prev2=nothing)
    k == 0 && return one(x)
    k == 1 && return 1 + alpha - x
    if prev == nothing
        prev = laguerre(k-1, alpha, x)
    end
    if prev2 == nothing
        prev2 = laguerre(k-2, alpha, x)
    end
    inv(base_ring(parent(x))(k)) * ((2k-1+alpha-x) * prev - (k+alpha-1) * prev2)
end

function laguerrebasis(k::Integer, alpha, x)
    v = Vector{typeof(one(alpha)*one(x))}(undef, 1+k)
    k == 0 && return v
    v[1] = one(x)
    k == 1 && return v
    v[2] = 1 + alpha - x
    for i = 3:k+1
        v[i] = laguerre(i-1, alpha, x, prev=v[i-1], prev2=v[i-2])
    end
    v
end

function binarysearch(f::Function, left::T, right::T, ndigits) where T
    while right-left > 1/big(10)^ndigits
        mid = (left+right)/2
        Printf.@printf("%1.10f\t%1.10f\n", left, right)
        if f(mid)
            right = mid
        else
            left = mid
        end
    end
    right
end

function lowerboundeigenvalue(X::arb_mat)
    F = base_ring(parent(X))
    for p = 1:100
        val = 1/F(10)^p
        Y = deepcopy(X)
        for i = 1:size(X, 1)
            Y[i,i] -= val
        end
        try 
            mycholesky(Y)
            return midpoint(val)-radius(val)
        catch
        end
    end
end

# int_a^b x^k e^(-pi x^2) dx
function intpolexp(k, a::arb, b::arb)
    F = parent(a)
    c = 1/(2sqrt(const_pi(F))^(k+1))
    l = myuppergamma(F(1+k)/2, const_pi(F) * a^2)
    r = myuppergamma(F(1+k)/2, const_pi(F) * b^2)
    c * (l - r)
end

################################################
### Code for percentage for simple/etc zeros ###
################################################

function r(problem, d, R, objv=nothing)
    F = ArbField(3000)
    R = F(R)
    S = AffineExpressionRing(F)
    _, u = PolynomialRing(S, "u")
    
    lag = laguerrebasis(2d+1, -F(1)/2, const_pi(F)*u)
    
    X = [psdvariable(S, d+1) for _=1:3]
    
    f = (R^2 - u) * quadform(X[1], lag[1:d+1])
    fhat = quadform(X[2], lag[1:d+1]) + u * quadform(X[3], lag[1:d+1])
    cib = coeffs_in_basis(fhat - sum(F(factorial(big(k))) / const_pi(F)^k * f.coeffs[1+k] * lag[1+k] for k=0:degree(f)), lag)
    
    if problem == :Z
        obj = R + 2/R * sum(f.coeffs[1+k] * intpolexp(2k+1, zero(R), R) for k=0:degree(f))
    elseif problem == :tildeZ
        obj = R + sum(f.coeffs[1+k] * (2/R*intpolexp(2k+1, zero(R), R) + 
                      3intpolexp(2k, R, 3R/2) - 2/R*intpolexp(2k+1, R, 3R/2)) for k=0:degree(f))
    elseif problem == :Z1
        obj = R + sum((2/R*intpolexp(2k+1, zero(R), R) - 8/R^2*intpolexp(2k+2, zero(R), R) +
                      sum(2^(2s+2) * F(factorial(big(s-1))) / F(factorial(big(2s))) / R^(2s+1) * 
                          intpolexp(2k+2s+1, zero(R), R) for s=1:15)) * f.coeffs[1+k] for k=0:degree(f))
    elseif problem == :L
        obj = R/2 + sum(f.coeffs[1+k] * (4/R*intpolexp(2k+1, zero(R), R/2) + 2intpolexp(2k, R/2, R)) for k=0:degree(f))
    else
        error("problem not supported")
    end

    if objv == nothing
        sdp = SparseSDP(Minimize(obj), f(0) - 1, fhat(0) - 1, cib...)
    else
        sdp = SparseSDP(obj - objv + psdvariable(S, 1)[1,1], f(0) - 1, fhat(0) - 1, cib...)
    end
    
    solver = SDPAGMP(precision=3000, epsilonstar="1e-30", epsilondash="1e-30", verbose=false)
    
    status, sol = solvesdp(sdp, solver)
    println(Float64(R), "\t", Float64(primalobj(sol)))
    objv == nothing ? primalobj(sol) : objv, [sol[M] for M in X]
end

function roptimize(problem, d)
    s = optimize(R -> r(problem, d, R)[1], big"1.0001", big"1.1", abs_tol=1e-7)
    Optim.minimum(s), Optim.minimizer(s)
end

function printmatrix(io, M)
    print(io, '[')
    for i = 1:size(M,1)
        for j = 1:size(M,2)
            Printf.@printf(io, "%.100e", BigFloat(M[i,j]))
            if j != size(M, 2)
                print(io, ' ')
            end
        end
        if i != size(M,1)
            print(io, "; ")
        end
    end
    print(io, ']')
end

function rstore(problem, d; R=nothing)
    obj, R = roptimize(problem, d)
    obj += big"1e-6"
    _, X = r(problem, d, R, obj)
    open("$(string(problem))-$d.txt", write=true) do f
        Printf.@printf(f, "%.100e\n", R)
        for M in X
            printmatrix(f, M)
            println(f)
        end
    end
end

function parsematrix(F, s::String)
    rows = split(s, ";")
    S = MatrixSpace(F, length(rows), length(rows))
    M = zero(S)
    for i in eachindex(rows)
        row = [F(v) for v in split(rows[i])]
        for j in eachindex(row)
            M[i, j] = row[j]
        end
    end
    M
end

function rverify(problem, d)
    F = ArbField(1000)
    S = MatrixSpace(F, d+1, d+1)
    P, x = PolynomialRing(F, "x")
    v = laguerrebasis(2d+1, -F(1)/2, const_pi(F) * x)
    s = readlines("$(string(problem))-$d.txt")
    R = F(s[1])
    X = [parsematrix(F, l) for l in s[2:4]]
    eigs = [lowerboundeigenvalue(M) for M in X]
    @assert minimum(eigs) > 0

    b = minimum(eigs[2:3])
    
    f = (R^2 - x) * quadform(X[1], v[1:d+1])
    fhat = quadform(X[2], v[1:d+1]) + x * quadform(X[3], v[1:d+1])
    Tf = P(0)
    
    for k = 0:degree(f)
        Tf += F(factorial(big(k))) / const_pi(F)^k * coeff(f, k) * v[1+k]
    end
    
    basis = vcat([(R^2 - x) * v[i] * v[j] for i=1:d+1 for j in [i, i+1]])
    B = maximum(abs(x) for x in coeffs_in_basis(fhat-Tf, basis))
    
    @assert b > (2d+1) * B
    
    U = evaluate(f, 0)
    L = evaluate(Tf, 0)
    
    if problem == :Z
        Zf = R + 2/R * sum(coeff(f, k) * intpolexp(2k+1, F(0), R) for k=0:degree(f))
    elseif problem == :tildeZ
        Zf = R + sum(coeff(f, k) * (2/R*intpolexp(2k+1, F(0), R) + 
            3intpolexp(2k, R, 3R/2) - 2/R*intpolexp(2k+1, R, 3R/2)) for k=0:degree(f))
    elseif problem == :Z1
        Zf = R + sum((2/R*intpolexp(2k+1, zero(R), R) - 8/R^2*intpolexp(2k+2, zero(R), R) +
                      sum(2^(2s+2) * F(factorial(big(s-1))) / F(factorial(big(2s))) / R^(2s+1) * 
                          intpolexp(2k+2s+1, zero(R), R) for s=1:50)) * coeff(f, k) for k=0:degree(f)) + 1/F(10)^10
    elseif problem == :L
        Zf = R/2 + sum(coeff(f, k) * (4/R*intpolexp(2k+1, F(0), R/2) + 2intpolexp(2k, R/2, R)) for k=0:degree(f))
    end
    
    res = U/L*Zf
    
    Printf.@printf("%1.6f\t%1.6f\t%1.6f\t%1.6f\t%1.6f\n", BigFloat(R), BigFloat(res), BigFloat(2-res), BigFloat((2*F(19)/27+5-res)/6), BigFloat(3)/2 - BigFloat(res)/2)
end

#####################
### Code for gaps ###
#####################

function g(problem, d, R, Lambda, epsilon)
    F = ArbField(2000)
    R = F(R)
    Lambda = F(Lambda)
    epsilon = F(epsilon)
    S = AffineExpressionRing(F)
    _, u = PolynomialRing(S, "u")
    
    lag = laguerrebasis(2d+1, -F(1)/2, const_pi(F)*u)
    
    X = [psdvariable(S, d+1) for _=1:3]
    
    f = (R^2 - u) * quadform(X[1], lag[1:d+1])
    fhat = quadform(X[2], lag[1:d+1]) + u * quadform(X[3], lag[1:d+1])
    fsos = coeffs_in_basis(fhat - sum(F(factorial(big(k))) / const_pi(F)^k * f.coeffs[1+k] * lag[1+k] for k=0:degree(f)), lag)
    
    phi = -u + 1/R*u^2 + R/const_pi(F) * sum(F(factorial(big(k))) / const_pi(F)^k * fhat.coeffs[1+k] for k=0:degree(fhat))

    if problem == :P
        psi = -R/const_pi(F) * sum(F(factorial(big(k))) / const_pi(F)^k * fhat.coeffs[1+k] * sum(const_pi(F)^s / F(factorial(big(s))) * 1/R^(2s) * u^s for s=0:k) for k=0:degree(fhat))
        sdp = SparseSDP(f(0) - 1 + epsilon, fhat(0) - 1 - epsilon, fsos..., phi(Lambda) + psi(Lambda^2)*exp(-const_pi(F)*(Lambda/R)^2) - epsilon)
    elseif problem == :tildeP
        psi1(lambda) = sum(R/const_pi(F)^(k+1) * (-myuppergamma(k+1, const_pi(F)*(lambda/R)^2) + myuppergamma(k+1, const_pi(F)*(3lambda/2R)^2) - myuppergamma(k+1, const_pi(F) * (lambda/R)^2)) * coeff(fhat, k) for k=0:degree(fhat))
        psi2(lambda) = sum(3lambda/2const_pi(F)^(k+F(1)/2) * (myuppergamma(k+F(1)/2, const_pi(F)*(lambda/R)^2) - myuppergamma(k+F(1)/2, const_pi(F)*(3lambda/2R)^2)) * coeff(fhat, k) for k=0:degree(fhat))
        sdp = SparseSDP(f(0) - 1 + epsilon, fhat(0) - 1 - epsilon, fsos..., phi(Lambda) + psi1(Lambda) + psi2(Lambda) - epsilon)
    end
    
    solver = SDPAGMP(precision=2000, epsilonstar="1e-40", epsilondash="1e-40", verbose=false)
    status, sol = solvesdp(sdp, solver)
  
    status, [sol[M] for M in X]
end

function gfindlambda(problem, d, R, epsilon=0, lambdaleft=big"0.5", lambdaright=big"0.7")
    Printf.@printf("R = %1.10f\n", R)
    binarysearch(Lambda -> g(problem, d, R, Lambda, epsilon)[1], lambdaleft, lambdaright, 6)
end

function goptimize(problem, d, epsilon=0, lambdaleft=big"0.5", lambdaright=big"0.7", rleft=big"1.001", rright=big"1.01")
    s = optimize(R->gfindlambda(problem, d, R, epsilon, lambdaleft, lambdaright)[1], rleft, rright, abs_tol=1e-7)
    Optim.minimum(s), Optim.minimizer(s)
end

function gstore(problem, d; lambdaleft=big"0.5", lambdaright=big"0.7", rleft=big"1.001", rright=big"1.01")
    Lambda, R = goptimize(problem, d, 1e-10, lambdaleft, lambdaright, rleft, rright)
    Lambda += 1e-6
    _, X = g(problem, d, R, Lambda, 1e-10)
    open("$(string(problem))-$d.txt", write=true) do f
        Printf.@printf(f, "%.100e\n", R)
        for M in X
            printmatrix(f, M)
            println(f)
        end
        Printf.@printf(f, "%.100e\n", Lambda)
    end
end

function gverify(problem, d)
    F = ArbField(5000)
    S = MatrixSpace(F, d+1, d+1)
    P, x = PolynomialRing(F, "x")
    v = laguerrebasis(2d+1, -F(1)/2, const_pi(F) * x)
    s = readlines("$(string(problem))-$d.txt")
    R = F(s[1])	
    Lambda = F(s[5])
    X = [parsematrix(F, l) for l in s[2:end-1]]
    eigs = [lowerboundeigenvalue(M) for M in X]

    @assert minimum(eigs) > 0    

    b = minimum(eigs[2:3])
    
    f = (R^2 - x) * quadform(X[1], v[1:d+1])
    fhat = quadform(X[2], v[1:d+1]) + x * quadform(X[3], v[1:d+1])
    @assert evaluate(f, F(0)) < 1
    Tf = P(0)
    for k = 0:degree(f)
        Tf += F(factorial(big(k))) / const_pi(F)^k * coeff(f, k) * v[1+k]
    end
    @assert evaluate(Tf, F(0)) > 1
    
    basis = vcat([(R^2 - x) * v[i] * v[j] for i=1:d+1 for j in [i, i+1]])
    B = maximum(abs(x) for x in coeffs_in_basis(fhat-Tf, basis))
    
    @assert b > (2d+1) * B
    
    phi = -x + 1/R*x^2 + R/const_pi(F) * sum(coeff(fhat, k) * F(factorial(big(k))) / const_pi(F)^k for k=0:degree(fhat))
    
    if problem == :P
        psi = -R/const_pi(F) * sum(coeff(fhat, k) * F(factorial(big(k))) / const_pi(F)^k * sum(const_pi(F)^s/F(factorial(big(s))) * (1/R* x)^(2s) for s=0:k) for k=0:degree(fhat))
        @assert evaluate(phi, Lambda) + evaluate(psi, Lambda) * exp(-const_pi(F)*(Lambda/R)^2) > 0
    elseif problem == :tildeP
        psi1(lambda) = sum(R/const_pi(F)^(k+1) * (-myuppergamma(k+1, const_pi(F)*(lambda/R)^2) + myuppergamma(k+1, const_pi(F)*(3lambda/2R)^2) - myuppergamma(k+1, const_pi(F) * (lambda/R)^2)) * coeff(fhat, k) for k=0:degree(fhat))
        psi2(lambda) = sum(3lambda/2const_pi(F)^(k+F(1)/2) * (myuppergamma(k+F(1)/2, const_pi(F)*(lambda/R)^2) - myuppergamma(k+F(1)/2, const_pi(F)*(3lambda/2R)^2)) * coeff(fhat, k) for k=0:degree(fhat))
        @assert evaluate(phi, Lambda) + psi1(Lambda) + psi2(Lambda) > 0
    end
end

#######################
### Other functions ###
#######################

function addmonomialcoeffs(problem, d)
    F = ArbField(3000)
    S = MatrixSpace(F, d+1, d+1)
    P, x = PolynomialRing(F, "x")
    v = laguerrebasis(2d+1, -F(1)/2, const_pi(F) * x)
    s = readlines("$(string(problem))-$d.txt")
    R = F(s[1])
    X = [parsematrix(F, l) for l in s[2:4]]
    f = (R^2 - x) * quadform(X[1], v[1:d+1])
    open("$(string(problem))-$d.txt", append=true) do file
        print(file, '[')
        for k = 0:degree(f)
            Printf.@printf(file, "%.100e", BigFloat(coeff(f, k)))
            if k != degree(f)
                print(file, ", ")
            end
        end
        println(file, ']')        
    end
end

end
