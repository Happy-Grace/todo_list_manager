"""
 Handles all files operations:
 ---> Creates files
 ---> Reads from files
 ---> Saves to files
 ---> Loads files
"""


# IMPORTS
from pathlib import Path
from constants import DATA_FOLDER, NAMES_FILE, ACTIVE_FILE, COMPLETED_FILE, DELETED_FILE
# from utils import user_input



# CREATE FOLDER FUNCTION
def create_data_folder() -> None:
    """
    Creates a folder to store the data files if it doesn't already exist.
    returns: None
    """
    
    if not DATA_FOLDER.exists():
        DATA_FOLDER.mkdir()



# GET SAVED USERNAMES FUNCTION
def get_saved_usernames() -> list[str]:
    """
    Gets all saved username
    returns: list of usernames
    """

    if not NAMES_FILE.exists():
        return []
    
    # OPEN IF IT EXISTS
    with NAMES_FILE.open("r", encoding="utf-8",) as file:
        
        names: list[str] = file.read().splitlines()
    
    return names



# SAVE USERNAMES FUNCTION
def save_usernames(username: str) -> None:
    """
    Save usernames if it is new.
    parameter: username
    returns: None
    """

    saved_names: list = get_saved_usernames()

    if username not in saved_names:
        with NAMES_FILE.open("a", encoding="utf-8",) as file:
            file.write(f"{username}\n")



# CREATE TASK FILES FUNCTION
def create_files() -> None:
    """
    Creates text files if they do not exist.
    """

    task_files: list[Path] = [
        ACTIVE_FILE, 
        COMPLETED_FILE, 
        DELETED_FILE
    ]

    for file in task_files:
        if not file.exists():
            file.touch()



# LOAD TASK FILES FUNCTION
def load_task(file_path: Path) -> list[dict]:
    """
    Load tasks from data file
    parameter: file_path[Path]
    return: list[dict]
    """

    # Create an empty list of dictionaries
    tasks: list[dict] = []

    # Load tasks from file
    with file_path.open("r", encoding="utf-8",) as file:

        lines: list[str] = file.read().splitlines()
        # LOOP AND LOADS
        for line in lines:
            task_data: list[str] = line.split("|")

            task: dict = {
                "task_id": int(task_data[0]), 
                "task_name": task_data[1], 
                "task_status": task_data[2], 
                "time_created": task_data[3], 
                "time_finished": task_data[4]
            }

            tasks.append(task)

    return tasks



# SAVE TASKS INTO FILE DOC.
def save_tasks(file_path: Path, tasks: list[dict]) -> None:
    """
    Save tasks into file
    :param file_path:
        Path to the task file.

    :param tasks:
        List of task dictionaries.

    return: None
    """

    with file_path.open("w", encoding="utf-8") as file:
        
        for task in tasks:
            task_line: str = (
                f"{task['task_id']}|"
                f"{task['task_name']}|"
                f"{task['task_status']}|"
                f"{task["time_created"]}|"
                f"{task["time_finished"]}\n"
            )

            file.write(task_line)


