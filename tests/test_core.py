from wip.core import (
    start_task,
    stop_task,
    resume_task,
    get_active,
    get_history,
    get_stats,
    undo_last,
    clear_all,
)


def test_start_task():
    clear_all()
    success, result = start_task("Test task")
    assert success is True
    assert result["task"] == "Test task"
    assert "id" in result


def test_multiple_tasks():
    clear_all()
    start_task("Task 1")
    start_task("Task 2")
    active = get_active()
    assert len(active) == 2


def test_stop_task():
    clear_all()
    start_task("Test task")
    success, result = stop_task()
    assert success is True
    assert result["task"] == "Test task"
    assert result["duration_minutes"] >= 0


def test_stop_by_id():
    clear_all()
    _, t1 = start_task("Task 1")
    start_task("Task 2")
    success, result = stop_task(t1["id"])
    assert success is True
    assert result["task"] == "Task 1"
    assert len(get_active()) == 1


def test_resume():
    clear_all()
    start_task("Test task")
    stop_task()
    success, result = resume_task()
    assert success is True
    assert result["task"] == "Test task"


def test_get_history():
    clear_all()
    start_task("Test task")
    stop_task()
    history = get_history()
    assert len(history) == 1


def test_get_stats():
    clear_all()
    start_task("Test task")
    stop_task()
    stats = get_stats()
    assert stats is not None
    assert stats["total_tasks"] == 1


def test_undo_last():
    clear_all()
    start_task("Test task")
    stop_task()
    success, result = undo_last()
    assert success is True
    assert len(get_history()) == 0


def test_clear_all():
    start_task("Test task")
    clear_all()
    assert get_active() == []
    assert get_history() == []
