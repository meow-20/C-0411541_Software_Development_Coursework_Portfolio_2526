import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("400x400")

tasks = []

def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
        tasks.pop(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

root.mainloop()
