# Task-Manager-CLI-APP
A beginner-friendly Task Manager built using Python lists. Lets users add, view, complete, and delete tasks from the command line.
add


## This is a beginner-friendly command-line Task Manager built with Python. It allows users to:

- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks

Everything is stored using simple Python data structures like lists and dictionaries.

---

## Technologies Used

- Python 3
- Lists, Dictionaries, Loops, Functions
- Terminal (CLI-based interface)

## Issues I Faced & What I Learned

1. Consistent Naming

- Problem: I initially had typos like "funtion" and "dictionery" in comments and function names.

- Fix: Carefully reviewed all spelling and ensured consistent naming conventions (e.g., use_snake_case for function names).

💡 Lesson: Good naming improves readability and avoids confusion, especially in larger projects.


2. Input Validation

- Problem: Program crashed if the user entered letters instead of numbers for task selection.

- Fix: Wrapped all input() that expect integers inside try-except blocks to catch ValueError.

💡 Lesson: Always validate user input to make your program user-friendly and robust.

3. Reduce Code Duplication

- Problem: Repeated the same code like view_all_task() multiple times across functions.

- Fix: Created a helper function is_tasks_empty() to reduce repetition and check for empty task lists.

💡 Lesson: DRY (Don't Repeat Yourself) makes code cleaner and easier to maintain.


4. Function Documentation

- Problem: Functions had little or no explanation.

- Fix: Added proper Python docstrings (""" """) to each function explaining its purpose.

💡 Lesson: Good documentation helps others (and my future self) understand the code quickly.

5.  Code Structure (main() Function)
 
- Problem : Program logic was not wrapped in a main() function.

- Fix: Moved the main loop into a main() function and added the Python entry point:

💡 Lesson: This makes the program modular, testable, and more Pythonic.

