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

# funtion to mark task as done
def mark_done():
    view_all_task()
    index = int(input("\nEnter Task Number To Mark As Done : "))
    for idx , task in enumerate(tasks):
        if idx == index-1:
            task['done'] = True
    print(f"Marked '{task['title'] }' As Done.")

# function to delete task 
def delete_task():
    view_all_task()
    delete = int(input("\nEnter Task Number To Remove : "))
    if 1 <= delete <= len(tasks):
        # We use another variable (removed_task) to store the item returned by tasks.pop(delete-1) so that we can access its details (like the task's title) after removing it from the list.
        removed_task = tasks.pop(delete-1)  
        # removed_task is not the part of list anymore that's why we access it by using another variable.
        print(f"\nTask '{removed_task['title']}' Removed Successfully !")
    else:
        print("\nInvalid Task Number.")




while True:
    show_menu()

# user selection to perform task
    choice = int(input("\nEnter Task Number : "))
    if choice == 1:
        view_all_task()
    elif choice == 2:
        add_task()
    elif choice == 3:
        mark_done()
    elif choice == 5:
        delete_task()
    else:
        print("Invalid Task Number. TRY AGAIN!")
