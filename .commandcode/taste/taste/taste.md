# Taste
- Prefers terse, low-ceremony prompts ("ok go on", "ok keep going") and expects the agent to keep proceeding autonomously after the initial task rather than pausing for detailed confirmation. Confidence: 0.7
- Uses deepseek v4 pro (deepseek/deepseek-v4-pro) as the model for agents/subagents. Confidence: 0.9
- Prefers dark theme in the CLI/tooling. Confidence: 0.6
- Prefers default permissions — explicitly rejected auto-accept (permissions.defaultMode: auto-accept), keeping permissions at the default level. Confidence: 0.7
- Prefers aggressive parallel subagent dispatch — wants many subagents launched at once, each attacking the problem with a novel/different approach. Confidence: 0.8
- Expects graceful recovery and continuation after interruptions (e.g. a server crash): resume from committed state and re-dispatch dead/in-flight tasks rather than restarting from scratch. Confidence: 0.6
