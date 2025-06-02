# Task Manager "to-do-list" CLI-App

# list to store all tasks in dictionary
tasks = []

# a function who show all menu


def show_menu():
    """
    Displays the main menu options for the Task Manager CLI application.
    """
    print("\n=================== TASK MANAGER ====================\n")
    print("1. View All Tasks")
    print("2. Add Task")
    print("3. Mark As Done")
    print("4. Modify Status")
    print("5. Delete Task")
    print("6. Exit")

#  Helper Function to check weather list is empty or not


def is_tasks_empty():
    """
    Checks is the tasks list is empty.
    Prints a message if empty and returns True, otherwise returns false.
    """
    if not tasks:
        print("\nList Is Empty Now.")
        return True
    return False

# function to add new task


def add_task():
    """
    Adds a new task to the tasks list.
    Promots the user to enter a task title and appends it as a dictionary.
    """
    if not tasks:
        print("No Task Exists. Enter The First Task")
    title = input("\nWrite Your Task Here : ")
    tasks.append({'title': title, 'done': False})

# function to view all task


def view_all_task():
    """
    Display all tasks in the tasks list with their status.
    show a message if the list is empty.
    """
    print("\n=================== TASK LIST =====================\n")
    if not tasks:
        print("LIST IS EMPTY NOW !.")
    for idx, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {task['title']}  [{status}].")

# function to mark task as done


def mark_done():
    """
    Marks a selected task as done.
    Promotes the user for the task number and updates its status.
    """
    if is_tasks_empty():
        return
    view_all_task()
    try:
        index = int(input("\nEnter Task Number To Mark As Done : "))
        if 1 <= index <= len(tasks):
            if tasks[index - 1]['done']:
                print(f"Task '{tasks[index - 1]['title']}' is already marked as done.")
            else:
                tasks[index - 1]['done'] = True
                print(f"Marked '{tasks[index - 1]['title']}' As Done.")
        else:
            print("Invalid Task Number.")
    except ValueError:
        print("Please enter a valid number.")
# function to modify the status


def modify_status():
    """
    Modifies the status of a selected task.
    Prompts the user for the task number and sets its status to not done.
    If the task is already not done, prints a message.
    """
    if is_tasks_empty():
        return
    view_all_task()
    try:
        update = int(input("\nEnter Task Number To Update Status : "))
        if 1 <= update <= len(tasks):
            if not tasks[update - 1]['done']:
                print(f"\nTask '{tasks[update - 1]['title']}' not done yet.")
            else:
                tasks[update - 1]['done'] = False
                print(f"\nTask '{tasks[update - 1]['title']}' status updated to Not Done!")
        else:
            print("\nInvalid Task Number.")
    except ValueError:
        print("\nInvalid Task Number")

# function to delete task


def delete_task():
    """
    Delete the selected task form the tasks list.
    promots the user for the task number and remove it form ths list.
    """
    if is_tasks_empty():
        return
    view_all_task()
    try:
        delete = int(input("\nEnter Task Number To Remove : "))
        if 1 <= delete <= len(tasks):
            # We use another variable (removed_task) to store the item returned by tasks.pop(delete-1) so that we can access its details (like the task's title) after removing it from the list.
            removed_task = tasks.pop(delete-1)
            # removed_task is not the part of list anymore that's why we access it by using another variable.
            print(f"\nTask '{removed_task['title']}' Removed Successfully !")
        else:
            print("\nInvalid Task Number.")
    except ValueError:
        print("\nPlease Enter A Valid Task Number")


def main():
    """Main Loop for the Task Manager CLI APP."""
    while True:
        show_menu()
        # user selection to perform task
        # check input valid
        try:
            choice = int(input("\nEnter Task Number : "))
        except ValueError:
            print("\nInput Is Invalid. Try Again.")
            continue
        if choice == 1:
            view_all_task()
        elif choice == 2:
            add_task()
        elif choice == 3:
            mark_done()
        elif choice == 4:
            modify_status()
        elif choice == 5:
            delete_task()
        elif choice == 6:
            print("\n THANKS TO VISIT.")
            break   # to exit from the loop
        else:
            print("Invalid Task Number. TRY AGAIN!")


# very first execution
if __name__ == "__main__":
    main()
