import uuid
from typing import Dict

class Task:
    def __init__(self, title: str, description: str, category: str, 
                 due_date: str, priority: str):
        self.id:int = 0
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = "Не выполнена"
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status
        }