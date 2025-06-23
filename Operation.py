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
        if not self.task_list:
            print("No tasks to suggest.")
            return

        # Suggests the tasks with highest priority
        sorted_tasks = sorted(self.task_list, key=lambda task: task.priority, reverse=True)
        top_tasks = sorted_tasks[:3]
        print("Suggested Tasks (based on priority):")
        
        for task in top_tasks:
            print(task)

    def exit_app(self):
        print("Exiting the application. Goodbye!")
