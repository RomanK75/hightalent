from typing import List
import json
from src.classes.Task import Task

class TaskManager:
    def __init__(self, filename: str = "db/tasks.json"):
        self.filename = filename
        self.current_id = 0
        self.tasks: List[Task] = []
        self.load_tasks()
        
    def get_next_id(self) -> int:
        self.current_id += 1
        return self.current_id
    
    def load_tasks(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                tasks_data = json.load(f)
                for task_data in tasks_data:
                    task = Task(
                        task_data["title"],
                        task_data["description"],
                        task_data["category"],
                        task_data["due_date"],
                        task_data["priority"]
                    )
                    task.id = task_data["id"]
                    task.status = task_data["status"]
                    self.tasks.append(task)
                    self.current_id = max(self.current_id, int(task.id))
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([task.to_dict() for task in self.tasks], f, 
                     ensure_ascii=False, indent=2)