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
        print("You can enter up to two columns you'd like to sort by below. If nothing is entered, the default order in the document will be used.")
        column_first = input("Enter the first column you want to sort by: ")
        while column_first not in list(self.task_list.columns):
            print("Column doesn't exist!")
            column_first = input("Enter the first column you want to sort by: ")
        if column_first == "":
            print(self.task_list)
        else:
            columns = []
            columns.append(column_first)
            column_second = input("Enter the second column you want to sort by: ")
            while (column_second not in list(self.task_list.columns)
                   or column_second == column_first):
                if column_second not in list(self.task_list.columns):
                    print("Column doesn't exist!")
                elif column_second == column_first:
                    print("This column is already sorted!")
                column_second = input("Enter the second column you want to sort by: ")
            if column_second != "":
                columns.append(column_second)
            tasks_sorted = self.task_list.sort_values(by=columns)
            print(tasks_sorted)
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
