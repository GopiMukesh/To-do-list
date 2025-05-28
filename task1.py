# Initialize an empty list to store tasks
todo_list = []

def display_tasks():
    """Display the current to-do list."""
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{index}. {task['name']} [{status}]")

def add_task():
    """Add a new task to the to-do list."""
    task_name = input("Enter the task name: ")
    todo_list.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' added successfully!")

def mark_task_completed():
    """Mark a task as completed."""
    display_tasks()
    task_index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_index < len(todo_list):
        todo_list[task_index]["completed"] = True
        print(f"Task '{todo_list[task_index]['name']}' marked as completed!")
    else:
        print("Invalid task number.")

def remove_task():
    """Remove a task from the to-do list."""
    display_tasks()
    task_index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_index < len(todo_list):
        removed_task = todo_list.pop(task_index)
        print(f"Task '{removed_task['name']}' removed successfully!")
    else:
        print("Invalid task number.")

def main():
    """Main function to handle user input."""
    while True:
        print("\nTo-Do List Application")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Exiting the application. Have a productive day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
