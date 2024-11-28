from src.classes.TaskManager import TaskManager
from src.classes.Task import Task
import re
from typing import List


# Basic validator args (user input, expected type, format cheking)
def validator(prompt, expected_type=str, format=None):
    while True:
        value = input(prompt)
        if value:
            try:
                if expected_type == int:
                    return int(value)
                elif expected_type == str:
                    if format == "date":
                        date_pattern = r'^\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$'
                        if re.match(date_pattern, value):
                            return value
                    
                    elif format == "priority":
                        if value.lower() in ["низкий", "средний", "высокий"]:
                            return value.capitalize()
                    else:
                        if value.strip():
                            return value
                    
                print(f"Неверный формат. Ожидается: {expected_type.__name__}")
                if format:
                    print(f"В формате: {format}")
                    
            except ValueError:
                print(f"Невозможно преобразовать '{value}' в {expected_type.__name__}")
        else:
            print("Введите значение.")

# Pagination for task view(tasks list, *page size, page state)
def display_tasks_page(tasks:List[Task], page_size=5, current_page=0):
    start_idx = current_page * page_size
    end_idx = start_idx + page_size
    page_tasks = tasks[start_idx:end_idx]
    if tasks:
        print(f"\nСтраница {current_page + 1} (задачи {start_idx + 1}-{min(end_idx, len(tasks))} из {len(tasks)})")
    else:
        print("Нет задач по данной категории.")
    
    for task in page_tasks:
        print(f"\nID: {task.id}")
        print(f"Название: {task.title}")
        print(f"Описание: {task.description}")
        print(f"Категория: {task.category}")
        print(f"Срок: {task.due_date}")
        print(f"Приоритет: {task.priority}")
        print(f"Статус: {task.status}")
        print("-" * 50)

# Main function
def main(file_path_to_json='db/tasks.json'):
    manager = TaskManager(file_path_to_json)
    while True:
        print("\n====== Менеджер задач ======")
        print("1. Просмотр задач")
        print("2. Добавить задачу")
        print("3. Изменить задачу")
        print("4. Удалить задачу")
        print("5. Поиск задач")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        # Exit
        if choice == "0":
            break
        # View tasks
        elif choice == "1":
            current_page = 0
            tasks = manager.get_tasks()
            tasks_filter = input("Введите название категории для фильтрации (или оставьте пустым для просмотра всех задач): ")
            if (tasks_filter):
                tasks = manager.get_tasks('category', tasks_filter)
            while True:
                display_tasks_page(tasks, current_page=current_page)
                if len(tasks) > (current_page + 1) * 5:
                    print("\n1 - Следующая страница")
                if current_page > 0:
                    print("2 - Предыдущая страница")
                print("0 - Вернуться в главное меню")
                
                nav_choice = input("\nВыберите действие: ")
                if nav_choice == "1" and len(tasks) > (current_page + 1) * 5:
                    current_page += 1
                elif nav_choice == "2" and current_page > 0:
                    current_page -= 1
                elif nav_choice == "0":
                    break
        # Add task
        elif choice == "2":
            title = validator("Введите название задачи: ")
            description = validator("Введите описание задачи: ")
            category = validator("Введите категорию задачи: ")
            due_date = validator("Введите срок (в формате ГГГГ-ММ-ДД): ", format="date")
            priority = validator("Введите приоритет (низкий, средний, высокий): ", format="priority")
            
            task = Task(title, description, category, due_date, priority)
            manager.add_task(task)
            print("ЗАДАЧА УСПЕШНО ДОБАВЛЕНА!")
            
        # Edit task
        elif choice == "3":
            task_id = validator("Введите ID задачи для редактирования: ", int)
            task = manager.get_tasks('id',task_id)
            if task:
                print(f"\n1. Изменить название(сейчас -> {task.title})")
                print(f"2. Изменить описание(сейчас -> {task.description})")
                print(f"3. Изменить категорию(сейчас -> {task.category})")
                print(f"4. Изменить срок(сейчас -> {task.due_date})")
                print(f"5. Изменить приоритет(сейчас -> {task.priority})")
                print(f"6. Изменить статус выполнения(сейчас -> {task.status})")
                print("-"*50)
                print("0. Вернуться в главное меню\n")
                
                edit_choice = input("Выберите действие: ")
                if edit_choice == "0":
                    break
                if edit_choice == "1":
                    task.title = validator("Новое название: ")
                elif edit_choice == "2":
                    task.description = validator("Новое описание: ")
                elif edit_choice == "3":
                    task.category = validator("Новая категория: ")
                elif edit_choice == "4":
                    task.due_date = validator("Новый срок (YYYY-MM-DD): ", format="date")
                elif edit_choice == "5":
                    task.priority = validator("Новый приоритет: ", format="priority")
                elif edit_choice == "6":
                    if task.status == "Не выполнена":
                        task.status = "Выполнена"
                    else:
                        task.status = "Не выполнена"
                
                manager.edit_task(task)
                print(f"ЗАДАЧА {task.id} ОБНОВЛЕНА!")
            else:
                print(f"ЗАДАЧА {task_id} НЕ НАЙДЕНА!")
        # Delete task by ID,NAME,CATEGORY
        elif choice == "4":
            delete_type = validator("Выберите тип удаления:\n1. По ID\n2. По категории\n0. Вернутся в меню\n", int)
            if delete_type == 0:
                break
            elif delete_type == 1:
                task_id = validator("Введите ID задачи для удаления: ", int)
                manager.delete_task(task_id)
            elif delete_type == 2:
                task_category = validator("Введите категорию задачи для удаления: ", str)
                manager.delete_task(task_category, 'category')

            
        # Search tasks by title, category, or status
        elif choice == "5":
            print("\n1. Поиск по названию")
            print("2. Поиск по категории")
            print("3. Поиск по статусу")
            print("-"*50)
            print("0. Вернуться в главное меню\n")
            
            search_choice = input("Выберите тип поиска: \n")
            while search_choice not in ["1", "2", "3", "0"]:
                print("ВВЕДЕН НЕ ВЕРНЫЙ НОМЕР!")
                print("1. Поиск по названию")
                print("2. Поиск по категории")
                print("3. Поиск по статусу")
                print("-"*50)
                print("0. Вернуться в главное меню\n")
                search_choice = input("Выберите тип поиска: \n")          
            if search_choice == "0":
                continue
            search_term = validator("Введите поисковый запрос: ")
            if search_choice == "1":
                tasks = manager.get_tasks('title', search_term)
            elif search_choice == "2":
                tasks = manager.get_tasks('category', search_term)
            elif search_choice == "3":
                tasks = manager.get_tasks('status', search_term)
            if tasks:
                for task in tasks:
                    print(f"ID: {task.id}")
                    print(f"Название: {task.title}")
                    print(f"Описание: {task.description}")
                    print(f"Категория: {task.category}")
                    print(f"Срок: {task.due_date}")
                    print(f"Приоритет: {task.priority}")
                    print(f"Статус: {task.status}")
                    print("-"*50)
            else:
                print("Задачи не найдены!")
        
        else:
            print("Неверный выбор. Попробуйте снова.")