from Task import Task
import pandas as pd


class TaskOperations:
    def __init__(self):
        self.task_list = []

    def add_task(self):
        print("Adding task")

    def remove_task(self):
        task_number = input("Enter the task number to remove: ")
        try:
            task_number = int(task_number)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        if task_number < 1 or task_number > len(self.task_list):
            print("Invalid task number.")
            return

        task = self.task_list[task_number - 1]
        self.task_list.remove(task)
        print(f"'{task.name}' has been removed from the list.")
        return

    def view_tasks(self):
        print("View tasks")

    def suggest_tasks(self):
        print("Suggesting tasks")

    def exit_app(self):
        print("Exiting the application. Goodbye!")
        df = pd.DataFrame([(task.name, task.deadline, task.priority) for task in self.task_list],
                          columns=['name', 'deadline', 'priority'])
        df.to_csv('task_list.csv', index=False)
        exit()
