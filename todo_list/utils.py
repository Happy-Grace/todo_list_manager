"""
Re-usable Helper Functions:
    ---> Banners
    ---> Pauses
    ---> Menu Display
    ---> Input Handling
"""

# iMPORTS
from constants import SEPARATOR, MARKER, MENU_OPTIONS
from file_handler import get_saved_usernames, save_usernames



# Greeting Message Function
def greeting_msg(title: str) -> None:
    """
    Displays a formatted welcome message to the user
    parameter: title
    returns: None.    
    """

    print(f"\n{MARKER}")
    print(f"\tWELCOME TO {title}")
    print(f"\n{MARKER}\n")



# Display Banner Function 
def display_banner(text: str) -> None:
    """
    Displays s formatted banner to the user
    parameter: text
    returns: None.
    """

    print(f"\t{text}")
    print(f"{SEPARATOR}")



# Display Menu Function: displays the menu options to the user.
def display_menu() -> None:
    """
    Displays the menu options to the user.
    returns: None
    """

    for i in range(len(MENU_OPTIONS)):
        print(f"{i + 1}. {MENU_OPTIONS[i]}")
    print()

# display_menu()



# Pause Program Function
def pause_program() -> None:
    """"
    Pauses program until user presses enter key
    returns: None
    """
    input(f"\nPress Enter to continue...")



# User's Input Function
def user_input() -> str:
    """
    Gets the user's input and returns it as a string.
    returns: str    
    """

    total_options = len(MENU_OPTIONS)

    choice: str = input(f"Select an option (1-{total_options}):").strip()
    return choice

# user_input()



# GET USRENAME FUNCTION
def username_input() -> str:
    """
    Asks for username
    retruns: string
    """

    username: str = input("Please enter your name: ").strip()
    return username.title()



# GREET USER FUNCTION
def  greet_user(username: str) -> None:
    """
    Greet user
    parameter: username
    returns: None
    """

    saved_names: list[str] = get_saved_usernames()

    if username in saved_names:
        print(f"\n Welcome back {username.upper()}! What can I do for you today?\n")

    else:
        print()
        print(f"\nHello {username.upper()} and welcome. How can I help you?\n")

        save_usernames(username)

    
