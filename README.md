# TDL (To-Do List) Project

In this project, you'll develop a console-based to-do list application. The application will provide a menu for the user to perform the following actions: 
1. Add a task to the to-do list. 
2. Remove a task from the to-do list. 
3. View all tasks in the to-do list. 
4. Exit the application. 

## 🚀 Features

1. Add Task: Allows the user to add a new task to the list. 
2. Remove Task: Allows the user to remove a task from the list. 
3. View Tasks: Displays all the tasks in the list. 
4. Exit: Ends the program. 

## 📁 Project Structure

```
TDL/
├── Main.py          # Entry point of the application
├── Task.py          # Task class definition
├── Operation.py     # Core operations and functionality
├── README.md        # Project documentation
```

## 🏗️ Architecture

### Task Class (`Task.py`)
- Represents a single task with attributes:
  - `name`: Task description
  - `deadline`: Due date for the task
  - `priority`: Priority level (integer, higher = more important)

### Operations Module (`Operation.py`)
Contains the core functionality:
- `add_task()`: Add new tasks to the list
- `remove_task()`: Remove tasks from the list
- `view_tasks()`: Display all tasks
- `edit_task()`: Modify existing tasks
- `suggest_tasks()`: Provide task suggestions

### Main Module (`Main.py`)
- Entry point of the application
- Initializes the To-Do List application
- Handles the main application flow

## 🎯 Usage

### Running the Application

```bash
python3 Main.py
```
