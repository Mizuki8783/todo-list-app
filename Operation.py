from Task import Task
import pandas as pd
import csv
import os

class TaskOperations:
    def __init__(self, csv_file="tasks-list.csv"):
        self.csv_file = csv_file
        self.task_list = []
        self.initialize_csv()
        self.load_from_csv()

    def initialize_csv(self):
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["name", "deadline", "priority"])

    def load_from_csv(self):
        with open(self.csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.task_list.append(Task(row["name"], row["deadline"], int(row["priority"])))

    def save_to_csv(self):
        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["name", "deadline", "priority"])
            for task in self.task_list:
                writer.writerow([task.name, task.deadline, task.priority])

    def add_task(self):
        name = input("Enter the task: ")
        self.task_list.append(Task(name))
        print(f"{name} has been added to the task list.")
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
