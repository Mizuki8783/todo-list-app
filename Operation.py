from Task import Task


class TaskOperations:
    def __init__(self):
        self.task_list = []

    def add_task(self):
        print("Adding task")

    def remove_task(self):
        task_name = input("Enter the task to remove: ")
        for task in self.task_list:
            if task.name == task_name:
                self.task_list.remove(task)
                print(f"'{task_name}' has been removed from the list.")
                return
        print(f"Task {task_name} not found")

    def view_tasks(self):
        print("View tasks")

    def suggest_tasks(self):
        print("Suggesting tasks")

    def exit_app(self):
        print("Exiting the application. Goodbye!")
        exit()
