from Task import Task
from datetime import datetime
from zoneinfo import ZoneInfo
import pandas as pd
import os
import keyboard

class TaskOperations:

    # Mapping of priority names to numeric values (lower number = higher priority)
    priority_map = {'high': 0, 'medium': 1, 'low': 2}

    def __init__(self, csv_file="tasks-list.csv"):
        # Initializes the task list and loads data from the CSV file
        self.csv_file = csv_file
        self.task_list = []
        self.load_from_csv()

    def get_priority_label(self, priority_num):
        return {v: k.capitalize() for k, v in self.priority_map.items()}[priority_num]

    def load_from_csv(self):
        # Load tasks from CSV file if it exists
        if os.path.exists(self.csv_file):
            try:
                df = pd.read_csv(self.csv_file)
                for _, row in df.iterrows():
                    # Convert each row into a Task object
                    self.task_list.append(Task(row["name"], row["deadline"], int(row["priority"])))
            except Exception as e:
                print("Failed to load tasks:", e)
        else:
            # If the file doesn't exist, create an empty one
            df = pd.DataFrame(columns=["name", "deadline", "priority"])
            df.to_csv(self.csv_file, index=False)
            print("No previous list was found, a new one was created!")

    def save_to_csv(self):
        # Save current tasks to the CSV file
        df = pd.DataFrame([
            {
                "name": task.name, 
                "deadline": task.deadline, 
                "priority": task.priority
            } for task in self.task_list
        ])
        df.to_csv(self.csv_file, index=False)

    def add_task(self):
        # Prompt user to enter task details
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

        # Add the task to the list and save
        self.task_list.append(Task(name, deadline, priority_num))
        print(f"'{name}' with priority '{priority}' and deadline '{deadline}' has been added to the list.")
        self.save_to_csv()

    def remove_task(self):
        # Prompt user to select a task number to remove
        task_number = input("Enter the task number to remove: ")
        try:
            task_number = int(task_number)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        if task_number < 1 or task_number > len(self.task_list):
            print("Invalid task number.")
            return

        # Remove the task and save the updated list
        task = self.task_list[task_number - 1]
        self.task_list.remove(task)
        print(f"'{task.name}' has been removed from the list.")
        self.save_to_csv()

    def view_tasks(self):
        # Display and optionally sort the list of tasks by selected columns
        columns = list(self.task_list[0].__dict__.keys())

        print("You can enter up to two columns you'd like to sort by below. If nothing is entered, the default order in the document will be used.")
        column_first = input("Enter the first column you want to sort by: ")
        
        # If no valid column is provided, show unsorted list
        while column_first not in columns:
            if column_first == "":
                print("To-Do List:")
                for i, task in enumerate(self.task_list):
                    print(f"{i + 1}. {task.name} - {self.get_priority_label(task.priority)} - {task.deadline}")
                break
            print("Column doesn't exist!")
            column_first = input("Enter the first column you want to sort by: ")
        else:
            # Allow second level sorting
            column_second = input("Enter the second column you want to sort by: ")
            while (column_second not in columns or column_second == column_first):
                if column_second == "":
                    # Sort by first column only
                    sorted_tasks = sorted(self.task_list, key=lambda task: getattr(task, column_first))
                    print("To-Do List:")
                    for i, sorted_task in enumerate(sorted_tasks):
                        print(f"{i + 1}. {task.name} - {self.get_priority_label(task.priority)} - {task.deadline}")
                    return
                if column_second not in columns:
                    print("Column doesn't exist!")
                elif column_second == column_first:
                    print("This column is already sorted!")
                column_second = input("Enter the second column you want to sort by: ")

            # Sort by two columns
            sorted_tasks = sorted(self.task_list, key=lambda task: (getattr(task, column_first), getattr(task, column_second)))
            print("To-Do List:")
            for i, sorted_task in enumerate(sorted_tasks):
                print(f"{i + 1}. {task.name} - {self.get_priority_label(task.priority)} - {task.deadline}")

    def suggest_tasks(self):
        while True:
            if not self.task_list:
                print("No tasks to suggest.")
                return

            # Ordenar por deadline (mais próximo primeiro), depois por prioridade
            sorted_tasks = sorted(
                self.task_list,
                key=lambda task: (
                    datetime.strptime(str(task.deadline), "%Y-%m-%d"),
                    task.priority
                )
            )

            # Cabeçalho com alinhamento
            print("\nSuggested Tasks (sorted by deadline and priority):\n")
            print(f"{'No.':<5} {'Task Name':<30} {'Deadline':<12} {'Priority':<10}")
            print("-" * 60)

            # Mostrar até 5 tarefas
            top_tasks = sorted_tasks[:5]
            for i, task in enumerate(top_tasks, 1):
                print(f"{i:<5} {task.name:<30} {str(task.deadline):<12} {self.get_priority_label(task.priority):<10}")

            print("\nTap any key to leave...")
            if keyboard.read_event().event_type == keyboard.KEY_DOWN:
                break
            

    def exit_app(self):
        # Save and exit the program
        print("Exiting the application. Goodbye!")
        self.save_to_csv()
        exit()
