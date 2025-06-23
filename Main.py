from Operation import TaskOperations


def main():
    print("To-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Task")
    print("4. Suggest Task")
    print("5. Exit")
    test = TaskOperations()
    test.add_task()
    
    # operation = input("Enter your choice: ")
    # try:
    #     operation = int(operation)
    # except ValueError:
    #     print("Invalid input. Please enter a number between 1 and 5.")
    #     return

    # if operation == 1:
    #     op.add_task()
    # elif operation == 2:
    #     op.remove_task()
    # elif operation == 3:
    #     op.view_tasks()
    # elif operation == 4:
    #     op.suggest_tasks()
    # elif operation == 5:
        # op.exit_app()


if __name__ == "__main__":
    main()
