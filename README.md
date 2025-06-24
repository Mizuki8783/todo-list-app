# TDL (To-Do List) Project

This is a console-based To-Do List application that allows users to manage their tasks efficiently through a simple menu system.

## 📋 Menu Options

1. Add a task to the to-do list  
2. Remove a task from the to-do list  
3. View all tasks (with optional sorting)  
4. Suggest tasks (by priority and deadline)  
5. Exit the application  

## 🚀 Features

- **Add Task**: Input task name, priority (`high`, `medium`, `low`), and deadline (`YYYY-MM-DD`).
- **Remove Task**: Delete a task by its position number.
- **View Tasks**: Display all tasks, optionally sorted by one or two attributes (`name`, `deadline`, `priority`).
- **Suggest Tasks**: Automatically suggests up to 5 tasks sorted by priority (high to low) and then by deadline (sooner first).
- **Persistent Storage**: Tasks are saved and loaded automatically from a CSV file using `pandas`.

## 📁 Project Structure

```
TDL/
├── Main.py          # Entry point of the application
├── Task.py          # Task class definition
├── Operation.py     # Core task operations
├── tasks-list.csv   # Data storage (auto-created)
├── README.md        # Project documentation
```

## 🏗️ Architecture

### Task Class (`Task.py`)
Represents a single task with the following attributes:
- `name`: Task description
- `deadline`: Due date in `YYYY-MM-DD` format
- `priority`: Numeric priority (0 = High, 1 = Medium, 2 = Low)

### Operations Module (`Operation.py`)
Contains core logic for managing tasks:
- `add_task()`: Create and validate a new task
- `remove_task()`: Remove task by number
- `view_tasks()`: Show tasks with optional multi-level sorting
- `suggest_tasks()`: Recommend tasks based on priority and deadline
- `exit_app()`: Save and exit

### Main Module (`Main.py`)
- Initializes and displays the main menu loop
- Handles user input and delegates actions to `TaskOperations`

## 💾 Requirements

- Python 3.9+
- [pandas](https://pypi.org/project/pandas/)

Install dependencies:

```bash
pip install pandas
```

## 🎯 Running the Application

```bash
python Main.py
```
