# Software Development Coursework Portfolio (2025/26)

## Disclaimer

In the file naming convention used in this repository:  
- **U** = Unit  
- **P** = Prepare  
- **T** = Task  
- **C** = Consolidate  

For example:  
- `U3PT1` → Unit 3 Prepare Task 1  
- `U3CT1` → Unit 3 Consolidate Task 1  

---

## Overview

This repository contains the **Software Development Coursework** for the academic year 2025/26. The assessment is divided into **two parts**:

- **Part A**: Collection of weekly worksheets, practical exercises, and tasks demonstrating Python programming concepts.
- **Part B**: Implementation of a **Command-Line Task Management System** in Python with features such as creating, viewing, managing, and persisting tasks.

---

## Repository Structure

PART_A/
├── U3PT1.py
├── U3CT1.py
├── U4PT1_1.py
├── U4PT1_2.py
├── U4PT1_3.py
├── U4CT1/
│   ├── inventory.csv
│   └── U4CT1.py
├── U5PT1.py
├── U5CT1.py
├── U6PT1/
│   ├── README.md
│   └── U6PT1.py
├── U6CT1.py
├── U7PT1.txt
├── U7CT1.py
├── U8PT1/
│   ├── U8PT1_1.py
│   ├── U8PT1_2.py
│   └── U8PT1_3.py
├── U9PT1.py

PART_B/
├── main.py
├── tasks.json
└── README.md

---

## Part A: Weekly Worksheets and Exercises

The **PART_A** folder contains multiple Python scripts and exercises, including:

- **U3PT1.py & U3CT1.py**: Calculations of areas of different shapes (rectangle, circle, triangle) with user input.
- **U4PT1_1.py, U4PT1_2.py, U4PT1_3.py**: Demonstrates arithmetic operations, data types, and variable manipulation.
- **U4CT1.py**: Inventory management system using CSV files with add, update, and display functionality.
- **U5PT1.py & U5CT1.py**: Interactive number and dice games demonstrating loops, random numbers, and conditional statements.
- **U6PT1/U6PT1.py**: UK Salary Calculator for 2025/26 computing net pay, income tax, NI contributions, and pension deductions.
- **U6CT1.py**: Basic to-do list manager (Part A prototype).
- **U7PT1.txt**: Pseudocode exercises for daily and weekly tasks.
- **U7CT1.py**: Number guessing game with input validation and attempts tracking.
- **U8PT1/**: Recursive functions exercises including factorial, Fibonacci sequence, and text-based fractals.
- **U9PT1.py**: GUI-based To-Do List using `tkinter` with add and delete functionality.

> Part A demonstrates basic to advanced Python concepts including variables, loops, conditionals, functions, recursion, file handling, and simple GUI programming.

---

## Part B: Command-Line Task Management System

The **PART_B** folder contains a **task management system** with the following features:

### Features

- **Add New Tasks**: Users can create new tasks with:
  - Title
  - Deadline (validated to prevent invalid dates or past deadlines)
  - Priority (1 = High, 2 = Medium, 3 = Low)
- **View Tasks**: List all tasks showing title, deadline, priority, and completion status.
- **Mark Tasks as Completed**: Update task status from incomplete to complete.
- **Delete Tasks**: Remove tasks by selecting their number from the list.
- **Sort Tasks**: 
  - By Deadline
  - By Priority
- **Persistent Storage**: Tasks are saved to `tasks.json` using file I/O.
- **Error Handling**: Handles invalid input, invalid dates, and out-of-range task numbers.

### File Descriptions

- **main.py**: Main program containing all functionality of the task manager.
  - Functions:
    - `load_tasks()`: Loads tasks from `tasks.json` safely.
    - `save_tasks(tasks)`: Saves tasks to `tasks.json`.
    - `get_valid_deadline()`: Validates date input and prevents past deadlines.
    - `add_task(tasks)`: Adds a new task with title, deadline, priority, and default completion status.
    - `view_tasks(tasks)`: Displays all tasks in a formatted list.
    - `complete_task(tasks)`: Marks a selected task as completed.
    - `delete_task(tasks)`: Deletes a selected task from the list.
    - `sort_by_deadline(tasks)`: Sorts tasks by their deadlines.
    - `sort_by_priority(tasks)`: Sorts tasks by their priority.
    - `show_menu()`: Displays the CLI menu.
    - `main()`: Runs the main program loop.
- **tasks.json**: Stores tasks persistently in JSON format.
- **README.md**: Instructions and project overview.

### Example CLI Menu

**Task Manager**

1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Sort by Deadline
6. Sort by Priority
7. Save File

---

## Technologies Used

- Python 3
- JSON (file handling for data persistence)
- Command-Line Interface (CLI)

---

## Purpose

This project demonstrates:

- Python programming concepts (variables, loops, conditionals, functions, recursion)
- File I/O and data persistence
- Input validation and error handling
- Structured, modular coding
- CLI and GUI interaction (Part A & B)

---

## Author

- **Name**: Bansari Panchal  
- **Module**: Software Development Coursework 2025/26  
- **GitHub**: https://github.com/meow-20

---
