from datetime import date
from typing import Optional

class Task:
    def __init__(self, name: str, deadline: Optional[date] = None, priority: int = 0):
        self.name = name
        self.priority = priority
        self.deadline = deadline

    def __str__(self):
        deadline_str = self.deadline.strftime('%Y-%m-%d') if self.deadline else "N/A"
        return f"Name: {self.name}, Priority: {self.priority}, Deadline: {deadline_str}"

    def __repr__(self):
        return self.__str__()
