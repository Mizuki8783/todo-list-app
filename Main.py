from Operation import TaskOperations

def main():
    to = TaskOperations()

    while True:
        print("\nTo-Do List Application")
        to.view_tasks()
        print()
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Sort Task")
        print("4. Suggest Task")
        print("5. Exit")
        print("6. Clean Terminal")

        try:
            operation = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue
        except Exception:
            print("An unexpected error occurred.")
            continue

        if operation == 1:
            to.add_task()
        elif operation == 2:
            to.remove_task()
        elif operation == 3:
            to.sort_tasks()
        elif operation == 4:
            to.suggest_tasks()
        elif operation == 5:
            to.exit_app()
            break
        elif operation == 6:
            to.clear_screen()
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()