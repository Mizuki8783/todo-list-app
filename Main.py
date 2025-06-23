from Operation import TaskOperations
from Task import Task


def main():
    print("To-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Task")
    print("4. Suggest Task")
    print("5. Exit")
    to = TaskOperations()

    while True:
        try:
            operation = input("Enter your choice: ")
            operation = int(operation)
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        except:  # noqa: E722
            print("Occur some input error")
            break

    if operation == 1:
        name = input("Enter the task: ")
        to.add_task(Task(name))


if __name__ == "__main__":
    main()
