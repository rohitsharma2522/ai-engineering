# Coding Agent: Flow and Examples

## What is this coding agent?

The coding agent is like ChatGPT with tools for working with files and running commands.

It can:

- Read files
- List files and folders
- Create files
- Edit files
- Run terminal commands
- Start and stop background servers

The agent does not directly change files by itself. The language model decides which tool to use, and the tool performs the action.

## Basic flow

```text
User request
    ↓
Language model understands the request
    ↓
Language model chooses a tool
    ↓
Safety middleware checks the tool request
    ↓
User approval is requested for risky actions
    ↓
Tool performs the action
    ↓
Result is sent back to the language model
    ↓
Agent explains what happened
```

## Example: creating a file

User request:

```text
Create hello.py that prints Hello, World.
```

The agent uses the `write_file` tool:

```text
write_file(
    path="hello.py",
    content="print('Hello, World!')"
)
```

The file is created at:

```text
05-CodingAgentMVP1/workspace/hello.py
```

## Example: reading a file

User request:

```text
Read hello.py and explain it.
```

The agent uses:

```text
read_file(path="hello.py")
```

Reading a file does not require human approval.

## Example: listing files

User request:

```text
Show me all files in the workspace.
```

The agent uses:

```text
list_files(path=".")
```

## Example: editing a file

User request:

```text
Change the greeting in hello.py to Good morning.
```

The agent uses the `edit_file` tool to replace the old text with the new text.

Because this changes a file, the human-in-the-loop middleware asks for approval first.

## Example: running a command

User request:

```text
Run hello.py.
```

The agent uses:

```text
run_command(command="python hello.py")
```

The command runs from the workspace directory. Commands that modify the computer or start a server require approval.

## Workspace limitation

The default working directory is:

```text
05-CodingAgentMVP1/workspace/
```

Relative paths are resolved inside this folder. For example:

```text
hello.py       → workspace/hello.py
src/app.py     → workspace/src/app.py
```

The agent rejects paths that try to escape the workspace, such as:

```text
../../secret.txt
```

The working directory can be changed with the `WORK_DIR` environment variable.

## Available tools

| Tool | Purpose | Approval usually required? |
|---|---|---|
| `list_files` | List files and folders | No |
| `read_file` | Read a text file | No |
| `write_file` | Create or overwrite a file | Yes |
| `edit_file` | Replace text in a file | Yes |
| `run_command` | Run a terminal command | Yes |
| `list_jobs` | Show background jobs | No |
| `stop_job` | Stop a background job | No |

## Safety checks

Before a tool runs, the agent checks:

1. Is the path inside the workspace?
2. Is the path protected, such as `.env`, `.git`, or a private key?
3. Does the file content contain suspicious code?
4. Is the command potentially dangerous?
5. Does the user need to approve the action?

Tool activity is also written to:

```text
workspace/.agent_audit.log
```

## The main idea

The agent follows this loop:

```text
Understand → Choose a tool → Check safety → Execute → Explain
```

That loop is what makes it a coding agent instead of a chatbot that only produces text.
