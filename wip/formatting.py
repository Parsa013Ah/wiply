from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.text import Text
from rich import box

console = Console()


def format_duration(minutes):
    if minutes < 60:
        return f"{int(minutes)}m"
    h = int(minutes // 60)
    m = int(minutes % 60)
    return f"{h}h {m}m" if m else f"{h}h"


def show_start(task_name, task_id):
    console.print(
        Panel(
            f"[bold green]▶ Started:[/bold green] {task_name}\n"
            f"[dim]ID: {task_id} | {datetime.now().strftime('%H:%M')}[/dim]",
            border_style="green",
            box=box.ROUNDED,
        )
    )


def show_stop(entry):
    duration = format_duration(entry["duration_minutes"])
    note = f"\n[dim]Note: {entry['note']}[/dim]" if entry["note"] else ""
    console.print(
        Panel(
            f"[bold red]■ Stopped:[/bold red] {entry['task']}\n"
            f"[bold]Duration:[/bold] {duration}{note}",
            border_style="red",
            box=box.ROUNDED,
        )
    )


def show_status(active):
    if not active:
        console.print(
            Panel(
                "[dim]Not working on anything[/dim]\n"
                "[dim]Start with: wip start <task>[/dim]",
                border_style="yellow",
                box=box.ROUNDED,
            )
        )
        return

    table = Table(box=box.ROUNDED, show_header=True, header_style="bold")
    table.add_column("ID", style="dim")
    table.add_column("Task", style="cyan")
    table.add_column("Elapsed", style="green", justify="right")

    for t in active:
        started = datetime.fromisoformat(t["started_at"])
        elapsed = (datetime.now() - started).total_seconds() / 60
        table.add_row(t["id"], t["task"], format_duration(elapsed))

    console.print(table)


def show_log(history):
    if not history:
        console.print("[dim]No history yet[/dim]")
        return

    table = Table(box=box.ROUNDED, show_header=True, header_style="bold")
    table.add_column("Task", style="cyan")
    table.add_column("Duration", style="green", justify="right")
    table.add_column("When", style="dim")
    table.add_column("Note", style="dim")

    for h in history:
        ended = datetime.fromisoformat(h["ended_at"])
        when = ended.strftime("%a %H:%M")
        table.add_row(
            h["task"],
            format_duration(h["duration_minutes"]),
            when,
            h["note"] or "",
        )

    console.print(table)


def show_stats(stats):
    if not stats:
        console.print(
            "[dim]No data yet. Start tracking with: wip start <task>[/dim]"
        )
        return

    summary = Table.grid(padding=(0, 2))
    summary.add_column(style="bold")
    summary.add_column()
    summary.add_row("Total time:", format_duration(stats["total_minutes"]))
    summary.add_row("Total tasks:", str(stats["total_tasks"]))
    summary.add_row("Today:", format_duration(stats["today_minutes"]))
    summary.add_row("Streak:", f"{stats['current_streak']} days")

    console.print(
        Panel(summary, title="[bold]Stats[/bold]", border_style="blue")
    )

    if stats["daily"]:
        console.print("\n[bold]Last 7 days:[/bold]")
        daily = stats["daily"]
        max_val = max(daily.values()) if daily else 1
        for day in sorted(daily.keys(), reverse=True)[:7]:
            minutes = daily[day]
            bar_len = int((minutes / max_val) * 20) if max_val > 0 else 0
            bar = "█" * bar_len
            console.print(f"  {day} {bar} {format_duration(minutes)}")

    if stats["task_counts"]:
        console.print("\n[bold]Top tasks:[/bold]")
        sorted_tasks = sorted(
            stats["task_counts"].items(), key=lambda x: x[1], reverse=True
        )[:5]
        for task, count in sorted_tasks:
            console.print(f"  {task}: {count}x")


def show_undo(entry):
    console.print(
        Panel(
            f"[bold yellow]↩ Undone:[/bold yellow] {entry['task']}\n"
            f"[dim]This entry has been removed from history[/dim]",
            border_style="yellow",
            box=box.ROUNDED,
        )
    )


def show_clear():
    console.print(
        Panel(
            "[bold]All data cleared[/bold]",
            border_style="red",
            box=box.ROUNDED,
        )
    )


def show_export(history):
    if not history:
        console.print("[dim]Nothing to export[/dim]")
        return

    lines = ["## Work Log", ""]
    for h in history:
        ended = datetime.fromisoformat(h["ended_at"])
        lines.append(
            f"- **{h['task']}** ({format_duration(h['duration_minutes'])})"
            f" - {ended.strftime('%a %H:%M')}"
        )
        if h["note"]:
            lines.append(f"  > {h['note']}")

    console.print("\n".join(lines))


def show_resume(task_name, task_id):
    console.print(
        Panel(
            f"[bold green]▶ Resumed:[/bold green] {task_name}\n"
            f"[dim]ID: {task_id} | {datetime.now().strftime('%H:%M')}[/dim]",
            border_style="green",
            box=box.ROUNDED,
        )
    )


def show_alert(task_name, elapsed_minutes):
    console.print(
        Panel(
            f"[bold yellow]⏰ Alert:[/bold yellow] {task_name}\n"
            f"[dim]Running for {format_duration(elapsed_minutes)}[/dim]",
            border_style="yellow",
            box=box.ROUNDED,
        )
    )


def live_view(active, history, spinner_frame):
    spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    spin = spinner[spinner_frame % len(spinner)]

    content = Text()

    if not active:
        content.append("Not working on anything\n", style="dim")
        content.append("Start with: wip start <task>", style="dim")
    else:
        for t in active:
            started = datetime.fromisoformat(t["started_at"])
            elapsed = (datetime.now() - started).total_seconds() / 60
            content.append(f"{spin} ", style="bold cyan")
            content.append(f"[{t['id']}] ", style="dim")
            content.append(f"{t['task']}\n", style="cyan")
            content.append(f"   Elapsed: ", style="bold")
            content.append(f"{format_duration(elapsed)}\n", style="green")
            content.append(f"   Started at {started.strftime('%H:%M')}\n\n", style="dim")

    if history:
        content.append(f"\nLast: {history[-1]['task']} ({format_duration(history[-1]['duration_minutes'])})", style="dim")

    return Panel(
        content,
        title="[bold]wip live[/bold]",
        border_style="cyan",
        box=box.ROUNDED,
    )
