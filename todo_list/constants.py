#  Stores fixed values, separators, statuses, menu texts etc.
# Stores all constant values used for the to-do list project.

# IMPORTS
from pathlib import Path

MARKER: str = "*" * 50
SEPARATOR: str = "-" * 35

# Menu Options
MENU_OPTIONS: list[str] = [
    "Add Task", 
    "View Active Tasks", 
    "View Completed Tasks", 
    "View Deleted Tasks", 
    "Edit Task Name", 
    "Mark Task As Complete",
    "Delete Task",
    "Exit"
]

ACTIVE_STATUS: str = "Active"
COMPLETED_STATUS: str = "Completed"
DELETED_STATUS: str = "Deleted"


# DATA FOLDER
DATA_FOLDER: Path = Path("data_files")

NAMES_FILE: Path = DATA_FOLDER/"names.txt"

# USER FILES
# USER_FILE_SUFFIX: str = ".txt"

# Stores the files used for the to-do list project in a '.txt' file in constant values.\
ACTIVE_FILE: Path = DATA_FOLDER/"Active.txt"
COMPLETED_FILE: Path = DATA_FOLDER/"Completed.txt"
DELETED_FILE: Path = DATA_FOLDER/"Deleted.txt"

