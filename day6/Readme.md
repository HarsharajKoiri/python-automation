# Day 6 - To-Do List 

A simple **To-Do List** built with Python to help you manage your tasks. This app allows users to add, remove, and view tasks while saving them to a file for persistence.

---

## Features

- ✅ **Add tasks** to your to-do list
- ❌ **Remove tasks** by selecting their task number
- 📋 **View your current to-do list**
- 💾 **Save and load tasks** to and from a file (`tasks.txt`)

---

## How It Works

1. **Load Tasks:** The app loads tasks from `tasks.txt` at the start.
2. **Add Task:** You can add new tasks to the list.
3. **Remove Task:** You can remove a task by selecting its number.
4. **Save Tasks:** When you exit the app, your tasks are saved to `tasks.txt` to persist across sessions.

---

## Requirements

- Python 3.x

---

## How to Use

1. **Run the script** to start the To-Do List App.
2. The app will show a menu with options to:
   - View your to-do list.
   - Add a new task.
   - Remove a task.
   - Exit and save tasks.
3. **Add tasks** by entering their description when prompted.
4. **Remove tasks** by entering the task number shown.
5. The app will automatically **save your tasks** in `tasks.txt` when you exit.

---

## Example

```bash
To-Do List App
1. View To-Do List
2. Add a Task
3. Remove a Task
4. Exit
Enter your choice (1-4): 2
Enter the task to add: Buy pizza
Task 'Buy pizza' added to the list.
```
## Flow
```mathematics
Start
  |
  v
Show Main Menu:
  1. View To-Do List
  2. Add a Task
  3. Remove a Task
  4. Exit
  |
  v
Check User Input
  |
  v
+-------------------+      +-----------------+      +-----------------------+      +----------------+
| View To-Do List   | ---> | Add a Task      | ---> | Remove a Task         | ---> | Exit and Save  |
+-------------------+      +-----------------+      +-----------------------+      +----------------+
  |                         |                           |
  v                         v                           v
Show Current List         Ask for Task Description     Show Task List, Ask Task No.
  |                         |                           |
  v                         v                           v
Return to Menu            Add Task to List            Remove Selected Task
  |                         |                           |
  v                         v                           v
Loop or Exit             Save to `tasks.txt`           Update Task List
  |                                                      |
  v                                                      v
End (Exit)                                             Save to `tasks.txt`
```
