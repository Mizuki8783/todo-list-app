from Task import Task

test = Task("Test Task", "2023-10-01", 1)

print(test)
print(test.name)
print(test.priority)


def add_task():
    print("Adding task")


def remove_task():
    print("Removing task")


def view_tasks():
    print("View tasks")


def suggest_tasks():
    print("Suggesting tasks")


def edit_task():
    print("Editing task")
