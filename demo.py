import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from wiply.core import start_task, stop_task, get_active, get_history, get_stats
from wiply.formatting import show_start, show_stop, show_status, show_stats as display_stats, console
from rich.panel import Panel
from rich import box

console.clear()
console.print(Panel("[bold cyan]wiply demo[/bold cyan]", border_style="cyan", box=box.ROUNDED))
console.print()

import time

success, t1 = start_task("Building wiply")
show_start(t1["task"], t1["id"])
time.sleep(1.5)

success, t2 = start_task("Review code")
show_start(t2["task"], t2["id"])
time.sleep(1.5)

show_status(get_active())
time.sleep(2)

stop_task(t2["id"])
time.sleep(1.5)

stats = get_stats()
if stats:
    display_stats(stats)
time.sleep(2)
