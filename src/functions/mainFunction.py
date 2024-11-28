from src.classes.TaskManager import TaskManager
from src.classes.Task import Task

def display_tasks_page(tasks, page_size=5, current_page=0):
    start_idx = current_page * page_size
    end_idx = start_idx + page_size
    page_tasks = tasks[start_idx:end_idx]
    
    print(f"\nСтраница {current_page + 1} (задачи {start_idx + 1}-{min(end_idx, len(tasks))} из {len(tasks)})")
    
    for task in page_tasks:
        print(f"\nID: {task.id}")
        print(f"Название: {task.title}")
        print(f"Описание: {task.description}")
        print(f"Категория: {task.category}")
        print(f"Срок: {task.due_date}")
        print(f"Приоритет: {task.priority}")
        print(f"Статус: {task.status}")
        print("-" * 50)


def main():
    manager = TaskManager()
    while True:
        print("\n====== Менеджер задач ======")
        print("1. Просмотр задач")
        print("2. Добавить задачу")
        print("3. Изменить задачу")
        print("4. Удалить задачу")
        print("5. Поиск задач")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "0":
            break
            
        elif choice == "1":
            current_page = 0
            while True:
                display_tasks_page(manager.tasks, current_page=current_page)
                if len(manager.tasks) > (current_page + 1) * 5:
                    print("\n1 - Следующая страница")
                if current_page > 0:
                    print("2 - Предыдущая страница")
                print("0 - Вернуться в главное меню")
                
                nav_choice = input("\nВыберите действие: ")
                if nav_choice == "1" and len(manager.tasks) > (current_page + 1) * 5:
                    current_page += 1
                elif nav_choice == "2" and current_page > 0:
                    current_page -= 1
                elif nav_choice == "0":
                    break
                
        elif choice == "2":
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            category = input("Введите категорию задачи: ")
            due_date = input("Введите срок выполнения (YYYY-MM-DD): ")
            priority = input("Введите приоритет (Низкий/Средний/Высокий): ")
            
            task = Task(title, description, category, due_date, priority)
            task.id = manager.get_next_id()
            manager.tasks.append(task)
            manager.save_tasks()
            print("Задача успешно добавлена!")
            
        elif choice == "3":
            task_id = int(input("Введите ID задачи для изменения: "))
            for task in manager.tasks:
                if task.id == task_id:
                    print("\n1. Изменить название")
                    print("2. Изменить описание")
                    print("3. Изменить категорию")
                    print("4. Изменить срок")
                    print("5. Изменить приоритет")
                    print("6. Отметить как выполненную")
                    
                    edit_choice = input("Выберите действие: ")
                    
                    if edit_choice == "1":
                        task.title = input("Новое название: ")
                    elif edit_choice == "2":
                        task.description = input("Новое описание: ")
                    elif edit_choice == "3":
                        task.category = input("Новая категория: ")
                    elif edit_choice == "4":
                        task.due_date = input("Новый срок (YYYY-MM-DD): ")
                    elif edit_choice == "5":
                        task.priority = input("Новый приоритет: ")
                    elif edit_choice == "6":
                        task.status = "Выполнена"
                    
                    manager.save_tasks()
                    print("Задача обновлена!")
                    break
            else:
                print("Задача не найдена!")
                
        elif choice == "4":
            task_id = int(input("Введите ID задачи для удаления: "))
            for task in manager.tasks[:]:
                if task.id == task_id:
                    manager.tasks.remove(task)
                    manager.save_tasks()
                    print("Задача удалена!")
                    break
            else:
                print("Задача не найдена!")
                
        elif choice == "5":
            print("\n1. Поиск по названию")
            print("2. Поиск по категории")
            print("3. Поиск по статусу")
            
            search_choice = input("Выберите тип поиска: ")
            search_term = input("Введите поисковый запрос: ")
            
            found = False
            for task in manager.tasks:
                if (search_choice == "1" and search_term.lower() in task.title.lower()) or \
                   (search_choice == "2" and search_term.lower() == task.category.lower()) or \
                   (search_choice == "3" and search_term.lower() == task.status.lower()):
                    print(f"\nID: {task.id}")
                    print(f"Название: {task.title}")
                    print(f"Описание: {task.description}")
                    print(f"Категория: {task.category}")
                    print(f"Срок: {task.due_date}")
                    print(f"Приоритет: {task.priority}")
                    print(f"Статус: {task.status}")
                    found = True
                    
            if not found:
                print("Задачи не найдены!")
        
        else:
            print("Неверный выбор. Попробуйте снова.")