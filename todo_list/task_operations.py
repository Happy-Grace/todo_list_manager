"""
Handles tasks operations/actions:
    ---> Add task
    ---> Delete task
    ---> Edit/Update task
    ---> Mark task as completed
    ---> View active tasks
    ---> View completed tasks
    ---> View deleted tasks
    ---> Exit program ?
""" 

# IMPORTS
from datetime import datetime
from constants import ACTIVE_STATUS, COMPLETED_STATUS, DELETED_STATUS
from typing import Any
from constants import SEPARATOR, ACTIVE_FILE, COMPLETED_FILE, DELETED_FILE
from file_handler import save_tasks



# ADD TASK FUNCTION
def add_task(active_tasks: list[dict]) -> list[dict]:
    """
    Adds a task to the active tasks list.
    parameter: active_tasks
    returns: None
    """

    task_name: str = input(f"Please enter task name:").strip().title()
    
    # TASK ID
    for index, task in enumerate(active_tasks,start=1):
        task["task_id"] = index
    task_id: int = len(active_tasks) + 1

    new_task = {
        "task_id": task_id, 
        "task_name": task_name, 
        "task_status": ACTIVE_STATUS, 
        "time_created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "time_finished": None
    }

    active_tasks.append(new_task)
    save_tasks(ACTIVE_FILE, active_tasks)
    print(f"✅ Task: '{task_name}' has been added successfully.")
    print(f"Added task details: {new_task}\n")

    return active_tasks



# View Tasks Function
def view_tasks(tasks: list[dict[str, Any]], title: str) -> None:
    """
    Displays the tasks to the user.
    parameter: tasks
    returns: None
    """

    print(f"\t{title}")
    print(f"{SEPARATOR}")

    # If there are NO tasks
    if len(tasks) == 0:
        print(f"\nYou have NO tasks available.")
        return
    
    # If there are tasks, display them
    for task in tasks:
        # Time Finished Condition
        time_finished: str
        if task['time_finished'] is None:
            time_finished = "Not Completed"
        else:
            time_finished = task['time_finished']
        
        # Display Task Details
        print(f"\n Task ID: {task['task_id']}")
        print(f" Task Name: {task['task_name']}")
        print(f" Task Status: {task['task_status']}")
        print(f" Time Created: {task['time_created']}")
        print(f" Time Finished: {time_finished}")
        print(f"{SEPARATOR}")
    print()




# EDIT TASK FUNCTION
def edit_task(active_tasks: list[dict]) -> None:
    """
    Edits a task in the active tasks list.
    parameter: active_tasks
    returns: None
    """

    if len(active_tasks) == 0:
        print(f"\nYou have NO active tasks to edit.")
        return
    
    # User Input for Task ID to Edit
    id_input: str = input(f"Please enter the task ID to edit: ").strip()
    
    try:
        task_id: int = int(id_input)

    except ValueError:
        print(f"❌ Invalid ID Input. Please enter a valid task ID.")
        return
    
    # Loop to find ID and edit
    for task in active_tasks:
        if task['task_id'] == task_id:
            old_name: str = task['task_name']
            new_name: str = input(f"\nPlease enter the new task name: ").strip().title()
            task['task_name'] = new_name
            save_tasks(ACTIVE_FILE, active_tasks)
            print(f"\n✅ Task ID {task_id} has been updated successfully.\n")
            print(f"Task with ID '{task_id}' with old name '{old_name}' has been updated to new name '{new_name}.")
            print(f"Updated task details: {task}\n")
            return
        
    print(f"❌ Task ID {task_id} not found. Please enter a valid task ID.")



# MARK AS COMPLETED FUNCTION
def complete_task(active_tasks: list[dict], completed_tasks: list[dict]) -> None:
    """
    Marks a task as completed and moves it to the completed tasks list.
    parameter: active_tasks, completed_tasks
    returns: None
    """

    if len(active_tasks) == 0:
        print(f"\nYou have NO actie tasks to mark as completed.")
        return
    
    id_input: str = input(f"Please enter that task ID: ").strip()

    try:
        task_id: int = int(id_input)
    
    except ValueError:
        print(f"❌ Invalid ID Input. Please enter a valid task ID.")
        return
    
    # LOOP TO FIND AND COMMPLETE TASK
    for task in active_tasks:
        if task['task_id'] == task_id:

            # CHANGE STATUS
            task['task_status'] = COMPLETED_STATUS

            # UPDATE TIME FINISHED
            task['time_finished'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


            # APPEND TO COMPLETED TASKS
            completed_tasks.append(task)
            
            # DELETE FROM ACTIVE TASKS AND SAVE
            active_tasks.remove(task)

            
            # LOOP AND UPDATE TASK IDs
            for index, task in enumerate(active_tasks, start=1):
                task['task_id'] = index
            
            for index, task in enumerate(completed_tasks, start=1):
                task['task_id'] = index

            # SAVE TASKS
            save_tasks(COMPLETED_FILE, completed_tasks)
            save_tasks(ACTIVE_FILE, active_tasks)

            print(f"\nTask with ID {task_id} has been marked as completed.\n")
            print(f"Completed task details: {task}\n")
            return
        
    print(f"❌ Task: {task_id} not found. Please enter a valid task ID.\n")



# DELETE TASK FUNCTION
def delete_task(active_tasks: list[dict], deleted_tasks: list[dict]) -> None:
    """
    Deletes a task from the active tasks list and moves it to the deleted tasks list.
    parameter: active_tasks, deleted_tasks
    returns: None
    """

    if len(active_tasks) == 0:
        print(f"\nYou have NO active tasks to delete.")
        return
    
    id_input: str = input(f"Please enter the task ID to delete: ").strip()
    try:
        task_id: int = int(id_input)

    except ValueError:
        print(f"❌ Invalid ID Input. Please enter a valid task ID.\n")
        return
    
    # LOOP TO FIND AND DELETE TASK
    for task in active_tasks:
        if task['task_id'] == task_id:

            # CHANGE STATUS
            task['task_status'] = DELETED_STATUS

            # APPEND TO DELETED TASKS
            deleted_tasks.append(task)
            

            # DELETE FROM ACTIVE TASKS
            active_tasks.remove(task)

            # LOOP AND UPDATE TASK ID
            for index, task in enumerate(active_tasks, start=1):
                task['task_id'] = index
                
            for index, task in enumerate(deleted_tasks, start=1):
                task['task_id'] = index

            # SAVE TASKS
            save_tasks(DELETED_FILE, deleted_tasks)
            save_tasks(ACTIVE_FILE, active_tasks)

            print(f"\nTask with ID {task_id} has been deleted.\n")
            print(f"Deleted task details: {task}\n")
            return
        
    print(f"❌ Task: {task_id} not found. Please enter a valid task ID.\n")


    
        
    

    

    






