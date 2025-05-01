# To-Do List App in Python

def load_tasks(filename):
    """Load tasks from a file."""
    try:
        with open(filename, 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(filename, tasks):
    """Save tasks to a file."""
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def display_tasks(tasks):
    """Display the current to-do list."""
    if tasks:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("\nYour To-Do List is empty!")

def add_task(tasks, task):
    """Add a new task to the list."""
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task(tasks, task_number):
    """Remove a task from the list."""
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' removed from the list.")
    else:
        print("Invalid task number!")

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("\nTo-Do List App")
        print("1. View To-Do List")
        print("2. Add a Task")
        print("3. Remove a Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            task = input("Enter the task to add: ")
            add_task(tasks, task)
        elif choice == '3':
            display_tasks(tasks)
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(tasks, task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            save_tasks(filename, tasks)
            print("Your tasks have been saved. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
