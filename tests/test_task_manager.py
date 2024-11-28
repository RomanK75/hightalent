import pytest
from src.classes.Task import Task
from src.classes.TaskManager import TaskManager

def test_task_creation():
    task = Task(
        title="Test Task",
        description="Test Description",
        category="Test",
        due_date="2024-12-31",
        priority="Высокий"
    )
    assert task.title == "Test Task"
    assert task.status == "Не выполнена"

def test_task_manager():
    manager = TaskManager("test_tasks.json")
    task = Task(
        title="Test Task",
        description="Test Description",
        category="Test",
        due_date="2024-12-31",
        priority="Высокий"
    )
    manager.tasks.append(task)
    manager.save_tasks()
    
    new_manager = TaskManager("test_tasks.json")
    assert len(new_manager.tasks) == 1
    assert new_manager.tasks[0].title == "Test Task"
