# TO-DO LIST MANAGER/APP: BRAIN OF THE PROGRAM
# IMPORTS
from utils import greeting_msg, display_menu, display_banner, user_input, username_input, greet_user
from task_operations import add_task, edit_task, view_tasks, edit_task, complete_task, delete_task
from file_handler import create_data_folder, create_files, load_task
from constants import ACTIVE_FILE, COMPLETED_FILE, DELETED_FILE


def main() -> None:
    """
    Runs the main to-do program
    returns: None
    """

    # TO-DO LIST BANNER
    greeting_msg("TO-DO LIST MANAGER")

    # FUNCTION TO CREATE DATA FILES FOLDER
    create_data_folder()

    # CREATE FILES
    create_files()

    # GET USERNAME AND GREET
    username: str = username_input()

    greet_user(username)

    # Create a list of dictionaries to store the tasks and their statuses.
    active_tasks: list[dict] = load_task(ACTIVE_FILE)
    completed_tasks: list[dict] = load_task(COMPLETED_FILE)
    deleted_tasks: list[dict] = load_task(DELETED_FILE)

    run: bool = True
    while run:
            display_banner("Main Menu")
            display_menu()

            user_choice = user_input()
            if user_choice == "1":
                print("\nYou have selected Add Task.\n")
                active_tasks = add_task(active_tasks)
            elif user_choice == "2":
                print("\nYou have selected View Active Tasks.\n")
                view_tasks(active_tasks, "Active Tasks")
            elif user_choice == "3":
                print("\nYou have selected View Completed Tasks.\n")
                view_tasks(completed_tasks, "Completed Tasks")
            elif user_choice == "4":
                print("\nYou have selected View Deleted Tasks.\n")
                view_tasks(deleted_tasks, "Deleted Tasks")
            elif user_choice == "5":
                print("\nYou have selected Edit Task Name.\n")
                edit_task(active_tasks)
            elif user_choice == "6":
                print("\nYou have selected Mark Task As Complete.\n")
                complete_task(active_tasks, completed_tasks)
            elif user_choice == "7":
                print("\nYou have selected Delete Task.\n")
                delete_task(active_tasks, deleted_tasks)
            elif user_choice == "8":
                print("\nYou have selected Exit.\n")
                run = False
            else:
                print("\nInvalid choice. Please select a valid option from the menu.\n")


# Runs the main function when the script is executed
if __name__ == "__main__":
    main()




