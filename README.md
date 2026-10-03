# wiply

![demo](demo.gif)

**Your work, beautifully tracked.**

A stupidly simple CLI that helps you track what you're working on — with beautiful output that makes productivity feel good.

## Install

```bash
pip install wiply
```

## Quick Start

```bash
# Start working on something
wiply start "Building a CLI tool"

# Check what you're doing
wiply status

# Stop when done
wiply stop "Finished the core logic"

# Resume last task
wiply resume

# See your day
wiply log

# Get stats
wiply stats

# Live view with timer
wiply live
```

## Demo

```
$ wiply start "Building something cool"
╭──────────────────────────────────────╮
│ ▶ Started: Building something cool   │
│   10:30                              │
╰──────────────────────────────────────╯

$ wiply live
╭──────────── wiply live ────────────╮
│ ⠋ Working on: Building something cool │
│ Elapsed: 25m                         │
│ Started at 10:30                     │
│                                      │
│ Last: Code review (45m)              │
╰──────────────────────────────────────╯

$ wiply stop "Core logic done"
╭──────────────────────────────────────╮
│ ■ Stopped: Building something cool   │
│ Duration: 25m                        │
│ Note: Core logic done                │
╰──────────────────────────────────────╯

$ wiply resume
╭──────────────────────────────────────╮
│ ▶ Resumed: Building something cool   │
│   11:00                              │
╰──────────────────────────────────────╯

$ wiply log
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Task                                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Building something cool  25m  10:30  │
└──────────────────────────────────────┘

$ wiply stats
╭────────── Stats ──────────╮
│ Total time:   25m         │
│ Total tasks:  1           │
│ Today:        25m         │
│ Streak:       1 days      │
╰───────────────────────────╯
```

## Why wiply?

- **Beautiful** — Rich terminal output that makes tracking feel good
- **Simple** — 4 commands to rule them all
- **Private** — All data stored locally in `~/.wiply/`
- **Git-friendly** — Your log is just JSON, commit it if you want
- **Fast** — No accounts, no sync, no nonsense

## Commands

| Command | Description |
|---------|-------------|
| `wiply start <task>` | Start a task |
| `wiply stop [note]` | Stop current task |
| `wiply resume` | Resume last task |
| `wiply status` | Show current status |
| `wiply log` | Show work history |
| `wiply stats` | Show statistics |
| `wiply live` | Live view with timer |
| `wiply undo` | Undo last entry |
| `wiply export` | Export as markdown |
| `wiply clear` | Clear all data |

## Options

- `wiply live --alert 30` — Alert after 30 minutes (default: 25)
- `wiply log --days 14` — Show last 14 days (default: 7)

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

MIT

---

If you find wiply useful, consider giving it a star!
