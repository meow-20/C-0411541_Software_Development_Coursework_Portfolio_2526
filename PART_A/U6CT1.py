tasks = []

def add_task(task_list, task):
    """Add a new task to the list with status 'Not Completed'."""
    task_list.append({"task": task, "completed": False})
    print(f"✅ Task added: '{task}'\n")

def mark_completed(task_list, task_number):
    """Mark a specific task as completed based on its number in the list."""
    if 0 < task_number <= len(task_list):
        task_list[task_number - 1]["completed"] = True
        print(f"✔️ Task '{task_list[task_number - 1]['task']}' marked as completed.\n")
    else:
        print("❌ Invalid task number.\n")

def display_tasks(task_list):
    """Display all tasks with their status."""
    if not task_list:
        print("📝 Your to-do list is empty.\n")
        return
    print("=== Your To-Do List ===")
    for i, task in enumerate(task_list, start=1):
        status = "Completed ✅" if task["completed"] else "Not Completed ❌"
        print(f"{i}. {task['task']} - {status}")
    print("======================\n")

def main():
    while True:
        print("Choose an option:")
        print("1. Add a task")
        print("2. Mark a task as completed")
        print("3. Display all tasks")
        print("4. Exit\n")
        
        choice = input("Enter your choice (1-4): ")
        print()
        
        if choice == "1":
            task = input("Enter the task description: ")
            add_task(tasks, task)
        elif choice == "2":
            display_tasks(tasks)
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                mark_completed(tasks, task_number)
            except ValueError:
                print("❌ Please enter a valid number.\n")
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            print("👋 Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.\n")

# Run the program
if __name__ == "__main__":
    main()
