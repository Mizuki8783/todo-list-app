from Task import Task
from datetime import datetime
from zoneinfo import ZoneInfo
import pandas as pd
import os

class TaskOperations:

    priority_map = {'high': 0, 'medium': 1, 'low': 2}

    def __init__(self, csv_file="tasks-list.csv"):
        self.csv_file = csv_file
        self.task_list = []
        self.load_from_csv()

    def load_from_csv(self):
        if os.path.exists(self.csv_file):
            try:
                df = pd.read_csv(self.csv_file)
                for _, row in df.iterrows():
                    self.task_list.append(Task(row["name"], row["deadline"], int(row["priority"])))
            except Exception as e:
                print("Failed to load tasks:", e)
        else:
            df = pd.DataFrame(columns=["name", "deadline", "priority"])
            df.to_csv(self.csv_file, index=False)
            print(f"No previous list was found, a new one was created!")

    def save_to_csv(self):
        df = pd.DataFrame([{
            "name": task.name, 
            "deadline": task.deadline, 
            "priority": task.priority
                } for task in self.task_list])
        df.to_csv(self.csv_file, index=False)

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
            try:
                deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date. Please enter a valid date in YYYY-MM-DD format.")
                continue

            if deadline < datetime.now(ZoneInfo("Canada/Pacific")).date():
                print("Deadline cannot be in the past. Please enter a valid date.")
                continue
            break

        self.task_list.append(Task(name, deadline, priority_num))
        print(f"'{name}' with priority '{priority}' and deadline '{deadline}' has been added to the list.")
        self.save_to_csv()

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
        self.save_to_csv()

    def view_tasks(self):
        priority_reverse_map = {v: k.capitalize() for k, v in self.priority_map.items()}
        print("To-Do List:")
        for i, task in enumerate(self.task_list):
            print(f"{i + 1}. {task.name} - {priority_reverse_map[task.priority]} - {task.deadline}")

    def sort_tasks(self):
        # Nothing to sort
        if len(self.task_list) == 0:
            print("No tasks to sort.")
            return

        columns = list(self.task_list[0].__dict__.keys())
        print("Enter up to two columns to sort by. If nothing is entered, the list will follow the last sorting or the default order.")

        # First column input
        column_first = input("Enter the first column you want to sort by: ")
        # Check if the input value is an existing column
        while column_first not in columns:
            if column_first == "":
                return
            print("Column doesn't exist!")
            column_first = input("Enter the first column you want to sort by: ")

        # Second column input
        column_second = input("Enter the second column you want to sort by: ")
        # Check if the input value is an existing column or is the same as the first column input
        while column_second not in columns or column_second == column_first:
            if column_second == "":
                sorted_tasks = sorted(self.task_list,
                                      key=lambda task: getattr(task, column_first))
                self.task_list = sorted_tasks
                return
            if column_second not in columns:
                print("Column doesn't exist!")
            elif column_second == column_first:
                print("This column is already sorted!")
            column_second = input("Enter the second column you want to sort by: ")
        sorted_tasks = sorted(self.task_list, key=lambda task: (getattr(task, column_first),
                                                                getattr(task, column_second)))
        self.task_list = sorted_tasks

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
        self.save_to_csv()
        exit()
