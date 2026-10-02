import uuid
from datetime import datetime, timedelta
from .storage import load_data, save_data


def start_task(task_name):
    data = load_data()
    task = {
        "id": str(uuid.uuid4())[:8],
        "task": task_name,
        "started_at": datetime.now().isoformat(),
    }
    data["active"].append(task)
    save_data(data)
    return True, task


def stop_task(task_id=None, note=""):
    data = load_data()
    if not data["active"]:
        return False, "Nothing to stop"

    if task_id:
        task = next((t for t in data["active"] if t["id"] == task_id), None)
        if not task:
            return False, f"Task {task_id} not found"
    else:
        task = data["active"][-1]

    ended_at = datetime.now()
    started_at = datetime.fromisoformat(task["started_at"])
    duration = (ended_at - started_at).total_seconds() / 60
    entry = {
        "task": task["task"],
        "started_at": task["started_at"],
        "ended_at": ended_at.isoformat(),
        "note": note,
        "duration_minutes": round(duration, 1),
    }
    data["history"].append(entry)
    data["active"] = [t for t in data["active"] if t["id"] != task["id"]]
    save_data(data)
    return True, entry


def resume_task():
    data = load_data()
    if not data["history"]:
        return False, "No previous task to resume"
    last = data["history"][-1]
    task = {
        "id": str(uuid.uuid4())[:8],
        "task": last["task"],
        "started_at": datetime.now().isoformat(),
    }
    data["active"].append(task)
    save_data(data)
    return True, task


def get_active():
    return load_data()["active"]


def get_status():
    return load_data()["active"]


def get_history(days=7):
    data = load_data()
    cutoff = datetime.now() - timedelta(days=days)
    return [
        h
        for h in data["history"]
        if datetime.fromisoformat(h["ended_at"]) >= cutoff
    ]


def get_stats():
    data = load_data()
    history = data["history"]
    if not history:
        return None

    total_minutes = sum(h["duration_minutes"] for h in history)
    total_tasks = len(history)

    today = datetime.now().date()
    today_entries = [
        h
        for h in history
        if datetime.fromisoformat(h["ended_at"]).date() == today
    ]
    today_minutes = sum(h["duration_minutes"] for h in today_entries)

    task_counts = {}
    for h in history:
        task = h["task"]
        task_counts[task] = task_counts.get(task, 0) + 1

    daily = {}
    for h in history:
        day = datetime.fromisoformat(h["ended_at"]).strftime("%Y-%m-%d")
        daily[day] = daily.get(day, 0) + h["duration_minutes"]

    return {
        "total_minutes": total_minutes,
        "total_tasks": total_tasks,
        "today_minutes": today_minutes,
        "today_tasks": len(today_entries),
        "task_counts": task_counts,
        "daily": daily,
        "current_streak": _calculate_streak(daily),
    }


def _calculate_streak(daily):
    if not daily:
        return 0
    streak = 0
    today = datetime.now().date()
    for i in range(365):
        day = (today - timedelta(days=i)).strftime("%Y-%m-%d")
        if day in daily:
            streak += 1
        elif i == 0:
            continue
        else:
            break
    return streak


def undo_last():
    data = load_data()
    if not data["history"]:
        return False, "Nothing to undo"
    last = data["history"].pop()
    save_data(data)
    return True, last


def clear_all():
    save_data({"active": [], "history": []})
    return True
