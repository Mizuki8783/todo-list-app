from Operation import TaskOperations

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
        to.add_task()
    elif operation == 2:
        to.remove_task()
    elif operation == 3:
        to.view_tasks()
    elif operation == 4:
        to.suggest_tasks()
    elif operation == 5:
        to.exit_app()
    else:
        print("Invalid choice. Please select a number between 1 and 5.")
        

if __name__ == "__main__":
    main()
