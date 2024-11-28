from typing import List
import json
from src.classes.Task import Task


class TaskManager:
    def __init__(self, filename: str):
        self.filename = filename
        self.__current_id: int = 0
        self.__tasks: List[Task] = []
        self.load_tasks()

    def get_next_id(self) -> int:
        self.__current_id += 1
        return self.__current_id

    def get_tasks(
        self, filter_type: str = None, value: str | int | None = None
    ) -> List[Task] | Task:
        if filter_type is None:
            return self.__tasks

        match filter_type:
            case "id":
                return next(
                    (task for task in self.__tasks if task.id == value), None
                )
            case "category":
                return [
                    task
                    for task in self.__tasks
                    if value.lower() in task.category.lower()
                ]
            case "title":
                return [
                    task
                    for task in self.__tasks
                    if value.lower() in task.title.lower()
                ]
            case "description":
                return [
                    task
                    for task in self.__tasks
                    if value.lower() in task.description.lower()
                ]
            case "due_date":
                return [
                    task for task in self.__tasks if value in task.due_date
                ]
            case "priority":
                return [
                    task
                    for task in self.__tasks
                    if value.lower() in task.priority.lower()
                ]
            case "status":
                return [
                    task
                    for task in self.__tasks
                    if value.lower() == task.status.lower()
                ]

    def add_task(self, task: Task):
        task.id = self.get_next_id()
        self.__tasks.append(task)
        self.save_tasks()

    def edit_task(self, task: Task):
        edited_task = self.get_tasks("id", task.id)
        if edited_task:
            edited_task.title = task.title
            edited_task.description = task.description
            edited_task.category = task.category
            edited_task.due_date = task.due_date
            edited_task.priority = task.priority
            self.save_tasks()
            print(f"Задача {task.id} успешно изменена")
        else:
            print(f"Задача {task.id} не найдена")

    def delete_task(self, value: str | int, deleteBy: str = "id"):
        match deleteBy:
            case "id":
                task = self.get_tasks("id", value)
                if task:
                    self.__tasks.remove(task)
                    self.save_tasks()
                    print(f"Задача {value} успешно удалена")
                else:
                    print(f"Задача {value} не найдена")
            case "category":
                tasks = []
                for task in self.__tasks:
                    if value.lower() == task.category.lower():
                        tasks.append(task)
                if tasks:
                    for task in tasks:
                        self.__tasks.remove(task)
                    self.save_tasks()
                    print(f"Задачи категории {value} успешно удалены")
                else:
                    print(f"Задачи категории {value} не найдены")

    def load_tasks(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                tasks_data = json.load(f)
                for task_data in tasks_data:
                    task = Task(
                        task_data["title"],
                        task_data["description"],
                        task_data["category"],
                        task_data["due_date"],
                        task_data["priority"],
                    )
                    task.id = task_data["id"]
                    task.status = task_data["status"]
                    self.__tasks.append(task)
                    self.__current_id = max(self.__current_id, int(task.id))
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(
                [task.to_dict() for task in self.__tasks],
                f,
                ensure_ascii=False,
                indent=2,
            )
