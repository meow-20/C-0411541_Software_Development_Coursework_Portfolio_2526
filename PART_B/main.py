import json
from datetime import datetime

FILENAME = "tasks.json"

# -------------------- File Handling --------------------

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            content = file.read().strip()
            if not content:
                return []
            return json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file)

# -------------------- Task Functions --------------------

def get_valid_deadline():
    while True:
        deadline = input("Enter deadline (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(deadline, "%Y-%m-%d")
            if date.date() < datetime.now().date():
                print("Deadline cannot be in the past.")
                continue
            datetime.strptime(deadline, "%Y-%m-%d")
            return deadline
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def add_task(tasks):
    title = input("Enter task title: ")
    deadline = get_valid_deadline()

    try:
        priority = int(input("Enter priority (1 = High, 3 = Low): "))
        if priority < 1 or priority > 3:
            raise ValueError
    except ValueError:
        print("Invalid priority. Task not added.")
        return

    task = {
        "title": title,
        "deadline": deadline,
        "priority": priority,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['title']} | Due: {task['deadline']} | Priority: {task['priority']} | [{status}]")

def complete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to complete: ")) - 1
        tasks[index]["completed"] = True
        print("Task marked as completed!")
    except (ValueError, IndexError):
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(index)
        print(f"Task '{removed['title']}' deleted.")
    except (ValueError, IndexError):
        print("Invalid task number.")

# -------------------- Sorting Functions --------------------

def sort_by_deadline(tasks):
    tasks.sort(key=lambda t: t["deadline"])
    print("Tasks sorted by deadline.")

def sort_by_priority(tasks):
    tasks.sort(key=lambda t: t["priority"])
    print("Tasks sorted by priority.")

# -------------------- Menu --------------------

def show_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Sort by Deadline")
    print("6. Sort by Priority")
    print("7. Save File")

# -------------------- Main Program --------------------

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            sort_by_deadline(tasks)

        elif choice == "6":
            sort_by_priority(tasks)

        elif choice == "7":
            save_tasks(tasks)
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# -------------------- Entry Point --------------------

if __name__ == "__main__":
    main()
