# Task Manager "to-do-list" CLI-App

# list to store all tasks in dictionery
tasks = []

# a function who show all menu
def show_menu():
    print("\n=================== TASK MANAGER ====================\n")
    print("1. View All Tasks")
    print("2. Add Task")
    print("3. Mark As Done")
    print("4. Modify Task")
    print("5. Delete Task")
    print("6. Exit")

# function to add new task
def add_task():
    if not tasks:
        print("No Task Exists. Enter The First Task")
    title = input("\nWrite Your Task Here : ")
    tasks.append({'title' : title , 'done' : False})

# function to view all task
def view_all_task():
    print("\n=================== TASK LIST ====================\n")
    if not tasks:
        print("LIST IS EMPTY NOW !.")
    for idx , task in enumerate(tasks , start = 1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {task['title']}  [{status}].")

while True:
    show_menu()

# user selection to perform task
    choice = int(input("\nEnter Task Number : "))
    if choice == 1:
        view_all_task()
    elif choice == 2:
        add_task()
    else:
        print("Invalid Task Number. TRY AGAIN!")
