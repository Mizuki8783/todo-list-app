from Task import Task


class TaskOperations:
    def __init__(self):
        self.task_list = []

    def add_task(self):
        name = input("Enter the task: ")
        self.task_list.append(Task(name))
        print(f"{name} has been added to the task list.")

    def remove_task(self):
        print("Removing task")

    def view_tasks(self):
        print("View tasks")

    def suggest_tasks(self):
        print("Suggesting tasks")

    def exit_app(self):
        print("Exiting the application. Goodbye!")
