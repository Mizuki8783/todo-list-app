class Task:
    def __init__(self, name: str, deadline: str = "", priority: int = 0):
        self.name = name
        self.priority = priority
        self.deadline = deadline

    def __str__(self):
        return f"{self.name} - {self.priority} - {self.deadline}"

    def __repr__(self):
        return self.__str__()
