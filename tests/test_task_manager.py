import pytest
from src.classes.TaskManager import TaskManager
from src.classes.Task import Task

@pytest.fixture
def task_manager():
    manager = TaskManager("test_tasks.json")
    yield manager
    # Cleanup after tests
    manager.tasks.clear()
    manager.save_tasks()

def test_add_task(task_manager):
    task = Task(
        title="Test Task",
        description="Test Description",
        category="Test",
        due_date="2024-12-31",
        priority="Высокий"
    )
    task.id = task_manager.get_next_id()
    task_manager.tasks.append(task)
    
    assert len(task_manager.tasks) == 1
    assert task_manager.tasks[0].title == "Test Task"
    assert task_manager.tasks[0].status == "Не выполнена"

def test_complete_task(task_manager):
    # Add a task first
    task = Task(
        title="Complete Test",
        description="Test Description",
        category="Test",
        due_date="2024-12-31",
        priority="Высокий"
    )
    task.id = task_manager.get_next_id()
    task_manager.tasks.append(task)
    
    # Complete the task
    task_manager.complete_task(task.id)
    assert task_manager.tasks[0].status == "Выполнена"

def test_search_task(task_manager):
    # Add test tasks
    task1 = Task(
        title="Search Test 1",
        description="Test Description",
        category="Test",
        due_date="2024-12-31",
        priority="Высокий"
    )
    task2 = Task(
        title="Different Task",
        description="Test Description",
        category="Test",
        due_date="2024-12-31",
        priority="Высокий"
    )
    task1.id = task_manager.get_next_id()
    task2.id = task_manager.get_next_id()
    task_manager.tasks.extend([task1, task2])
    
    # Search for tasks
    found_tasks = [task for task in task_manager.tasks if "Search" in task.title]
    assert len(found_tasks) == 1
    assert found_tasks[0].title == "Search Test 1"

def test_delete_task(task_manager):
    # Add a task
    task = Task(
        title="Delete Test",
        description="Test Description",
        category="Test",
        due_date="2024-12-31",
        priority="Высокий"
    )
    task.id = task_manager.get_next_id()
    task_manager.tasks.append(task)
    
    # Delete the task
    initial_count = len(task_manager.tasks)
    task_manager.delete_task(task.id)
    assert len(task_manager.tasks) == initial_count - 1
    assert not any(t.id == task.id for t in task_manager.tasks)
