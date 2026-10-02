# wip

**Your work, beautifully tracked.**

A stupidly simple CLI that helps you track what you're working on — with beautiful output that makes productivity feel good.

## Install

```bash
pip install wip
```

## Quick Start

```bash
# Start working on something
wip start "Building a CLI tool"

# Check what you're doing
wip status

# Stop when done
wip stop "Finished the core logic"

# Resume last task
wip resume

# See your day
wip log

# Get stats
wip stats

# Live view with timer
wip live
```

## Demo

```
$ wip start "Building something cool"
╭──────────────────────────────────────╮
│ ▶ Started: Building something cool   │
│   10:30                              │
╰──────────────────────────────────────╯

$ wip live
╭──────────── wip live ────────────╮
│ ⠋ Working on: Building something cool │
│ Elapsed: 25m                         │
│ Started at 10:30                     │
│                                      │
│ Last: Code review (45m)              │
╰──────────────────────────────────────╯

$ wip stop "Core logic done"
╭──────────────────────────────────────╮
│ ■ Stopped: Building something cool   │
│ Duration: 25m                        │
│ Note: Core logic done                │
╰──────────────────────────────────────╯

$ wip resume
╭──────────────────────────────────────╮
│ ▶ Resumed: Building something cool   │
│   11:00                              │
╰──────────────────────────────────────╯

$ wip log
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Task                                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Building something cool  25m  10:30  │
└──────────────────────────────────────┘

$ wip stats
╭────────── Stats ──────────╮
│ Total time:   25m         │
│ Total tasks:  1           │
│ Today:        25m         │
│ Streak:       1 days      │
╰───────────────────────────╯
```

## Why wip?

- **Beautiful** — Rich terminal output that makes tracking feel good
- **Simple** — 4 commands to rule them all
- **Private** — All data stored locally in `~/.wip/`
- **Git-friendly** — Your log is just JSON, commit it if you want
- **Fast** — No accounts, no sync, no nonsense

## Commands

| Command | Description |
|---------|-------------|
| `wip start <task>` | Start a task |
| `wip stop [note]` | Stop current task |
| `wip resume` | Resume last task |
| `wip status` | Show current status |
| `wip log` | Show work history |
| `wip stats` | Show statistics |
| `wip live` | Live view with timer |
| `wip undo` | Undo last entry |
| `wip export` | Export as markdown |
| `wip clear` | Clear all data |

## Options

- `wip live --alert 30` — Alert after 30 minutes (default: 25)
- `wip log --days 14` — Show last 14 days (default: 7)

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

MIT

---

If you find wip useful, consider giving it a star!
