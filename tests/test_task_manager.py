import pytest
from src.classes.TaskManager import TaskManager
from src.classes.Task import Task

@pytest.fixture
def task_manager():
    manager = TaskManager("test_tasks.json")
    yield manager
    # Cleanup
    manager.delete_task("Test Category", "category")
    manager.save_tasks()

def test_add_task(task_manager):
    task = Task(
        title="Test Task",
        description="Test Description",
        category="Test Category",
        due_date="2024-12-31",
        priority="Высокий"
    )
    task_manager.add_task(task)
    
    found_task = task_manager.get_tasks('id', task.id)
    assert found_task is not None
    assert found_task.title == "Test Task"

def test_edit_task(task_manager):
    # First add a task
    task = Task(
        title="Original Title",
        description="Original Description",
        category="Test Category",
        due_date="2024-12-31",
        priority="Высокий"
    )
    task_manager.add_task(task)
    
    # Edit the task
    edited_task = Task(
        title="Updated Title",
        description="Updated Description",
        category="Test Category",
        due_date="2024-12-31",
        priority="Низкий"
    )
    edited_task.id = task.id
    task_manager.edit_task(edited_task)
    
    # Verify changes
    found_task = task_manager.get_tasks('id', task.id)
    assert found_task.title == "Updated Title"
    assert found_task.priority == "Низкий"

def test_delete_task_by_id(task_manager):
    task = Task(
        title="Delete Test",
        description="Test Description",
        category="Test Category",
        due_date="2024-12-31",
        priority="Высокий"
    )
    task_manager.add_task(task)
    
    task_manager.delete_task(task.id, 'id')
    found_task = task_manager.get_tasks('id', task.id)
    assert found_task is None

def test_delete_tasks_by_category(task_manager):
    tasks = [
        Task("Task 1", "Desc 1", "Category A", "2024-12-31", "Высокий"),
        Task("Task 2", "Desc 2", "Category A", "2024-12-31", "Средний")
    ]
    for task in tasks:
        task_manager.add_task(task)
    
    task_manager.delete_task("Category A", "category")
    found_tasks = task_manager.get_tasks('category', "Category A")
    assert len(found_tasks) == 0

def test_search_tasks(task_manager):
    task = Task(
        title="Search Test",
        description="Searchable Description",
        category="Test Category",
        due_date="2024-12-31",
        priority="Высокий"
    )
    task_manager.add_task(task)
    
    by_title = task_manager.get_tasks('title', 'Search')
    assert len(by_title) == 1
    
    by_description = task_manager.get_tasks('description', 'Searchable')
    assert len(by_description) == 1
    
    by_status = task_manager.get_tasks('status', 'Не выполнена')
    assert len(by_status) >= 1

def test_get_all_tasks(task_manager):
    initial_count = len(task_manager.get_tasks())
    
    new_task = Task(
        title="New Task",
        description="Description",
        category="Test Category",
        due_date="2024-12-31",
        priority="Высокий"
    )
    task_manager.add_task(new_task)
    
    all_tasks = task_manager.get_tasks()
    assert len(all_tasks) == initial_count + 1
