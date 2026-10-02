import time
from datetime import datetime
import click
from .core import (
    start_task,
    stop_task,
    resume_task,
    get_active,
    get_history,
    get_stats,
    undo_last,
    clear_all,
)
from .formatting import *


@click.group()
def cli():
    """wip - Your work, beautifully tracked."""
    pass


@cli.command()
@click.argument("task")
def start(task):
    """Start working on a task."""
    success, result = start_task(task)
    if success:
        show_start(result["task"], result["id"])
    else:
        console.print(f"[red]{result}[/red]")


@cli.command()
@click.argument("task_id", required=False)
@click.argument("note", required=False, default="")
def stop(task_id, note):
    """Stop a task (latest if no ID given)."""
    success, result = stop_task(task_id, note)
    if success:
        show_stop(result)
    else:
        console.print(f"[red]{result}[/red]")


@cli.command()
def resume():
    """Resume the last stopped task."""
    success, result = resume_task()
    if success:
        show_resume(result["task"], result["id"])
    else:
        console.print(f"[red]{result}[/red]")


@cli.command()
def status():
    """Show active tasks."""
    show_status(get_active())


@cli.command()
@click.option("--days", "-d", default=7, help="Number of days to show")
def log(days):
    """Show work log."""
    show_log(get_history(days))


@cli.command()
def stats():
    """Show statistics."""
    show_stats(get_stats())


@cli.command()
def undo():
    """Undo the last completed task."""
    success, result = undo_last()
    if success:
        show_undo(result)
    else:
        console.print(f"[red]{result}[/red]")


@cli.command()
def clear():
    """Clear all data."""
    clear_all()
    show_clear()


@cli.command()
@click.option("--days", "-d", default=7, help="Number of days to export")
def export(days):
    """Export work log as markdown."""
    show_export(get_history(days))


@cli.command()
@click.option("--alert", "-a", default=25, help="Alert after N minutes")
def live(alert):
    """Live view with timer and animation."""
    from .core import load_data

    console.clear()
    console.print("[bold cyan]wip live[/bold cyan] — Ctrl+C to exit\n")

    frame = 0
    last_alert = 0
    try:
        with Live(console=console, refresh_per_second=4, screen=True) as live:
            while True:
                data = load_data()
                active = data["active"]
                history = data["history"][-5:]

                live.update(live_view(active, history, frame))

                if active:
                    now = datetime.now()
                    for t in active:
                        started = datetime.fromisoformat(t["started_at"])
                        elapsed = (now - started).total_seconds() / 60
                        if elapsed >= alert and (elapsed - last_alert) >= alert:
                            last_alert = elapsed
                            console.print(
                                f"\n[yellow]⏰ {t['task']} running for {format_duration(elapsed)}[/yellow]\n"
                            )

                frame += 1
                time.sleep(0.25)
    except KeyboardInterrupt:
        console.print("\n[dim]Exited live view[/dim]")


def main():
    cli()
