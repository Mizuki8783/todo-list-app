from Task import Task
from datetime import datetime
from zoneinfo import ZoneInfo
import pandas as pd


class TaskOperations:
    priority_map = {'high': 0, 'medium': 1, 'low': 2}

    def __init__(self):
        self.task_list = []

    def add_task(self):
        name = input("Enter the task: ").strip()
        
        # Validate priority input
        while True:
            priority = input("Enter the task (high, medium, low): ").lower().strip()
            if priority in self.priority_map:
                break
            print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
        priority_num = self.priority_map[priority]
        
        # Validate deadline input
        while True:
            deadline = input("Enter the task (YYYY-MM-DD): ").strip()
            
            # Convert string to date object and check if it's valid
            try:
                deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date. Please enter a valid date in YYYY-MM-DD format.")
                continue

            # Check if the deadline is in the past
            if deadline < datetime.now(ZoneInfo("Canada/Pacific")).date():
                print("Deadline cannot be in the past. Please enter a valid date.")
                continue
            break
        
        self.task_list.append(Task(name, deadline, priority_num))
        print(f"'{name}' with priority '{priority}' and deadline '{deadline}' has been added to the list.")

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
        df = pd.DataFrame([(task.name, task.deadline, task.priority) for task in self.task_list],
                          columns=['name', 'deadline', 'priority'])
        df.to_csv('task_list.csv', index=False)
        exit()
