import sys
import os
import csv
from typing import Callable
from prompt_toolkit import prompt
from utility.addressbook import AddresBook
from utility.record import Record
from utility.name import Name
from utility.phone import Phone
from utility.email import Email
from utility.birthday import Birthday, FutureDateError
from utility.notes import Note
from utility.sorter import FileSorter
from utility.cmd_complet import CommandCompleter, similar_command
from utility.notes_interaction import *

# paths to files with data
ADDRESBOOK_DATA_PATH = os.path.join(os.getcwd(), "data/addresbook.dat") # Because it's a simple program. The path is hard coded ;)


#objects storing data while the program is running
ADDRESBOOK = AddresBook().load_addresbook(ADDRESBOOK_DATA_PATH)


#initialize an instance of FileSorter class
file_sorter = FileSorter()

#function for FileSorter in specified directory
def sort_files_in_directory(directory):
    file_sorter.process_folder(directory)

#functions for note command #================CHECK


        
# function to handle with errors
def error_handler(func: Callable):
    def wrapper(*args):
        while True:
            try:
                return func(*args)
            # błędy i komunikaty przeniesione z pierwotnej wersji - do sprawdzenia / zmiany
            except ValueError:
                if func.__name__ == "add_name":
                    print("The name field cannot be empty, try again.")
                if func.__name__ == "add_phone":
                    print("Invalid phone number, try again.")
                if func.__name__ == "add_email":
                    print("Invalid email, try again.")
                if func.__name__ == "add_birthday":
                    print("Invalid date format, try again.")
                if func.__name__ == "import_from_csv":
                    print("I can't import from this source. Check the file.")
                    break
            except FutureDateError:
                print("You can't use a future date as a birthday, try again.")
            except FileNotFoundError:
                print("I can't find file to import data.")
                break
            except KeyboardInterrupt:
                cli_pyassist_exit()
    return wrapper


# a function that parses user input commands
def parse_command(user_input: str) -> (str, tuple):
    """
    Parse user input command

    Args:
        user_input (str): user input command
    
    Returns:
        str: command
        tuple: arguments
    """
    tokens = user_input.split()
    command = tokens[0]
    arguments = tokens[1:]
    return command, tuple(arguments)

# taking a command from the user
def user_command_input(completer: CommandCompleter):
    user_input = prompt(">>> ", completer=completer).strip().lower()
    if user_input:
        return parse_command(user_input)

# exit / close program
def cli_pyassist_exit(*args):
    ADDRESBOOK.save_addresbook(ADDRESBOOK_DATA_PATH)
    NOTES.save_notes(NOTES_DATA_PATH)
    print("Your data has been saved.") 
    sys.exit("Good bye!")

    
# hendler for main menu
def get_main_handler(command):
    return MAIN_COMMANDS[command]

# function to handle sort command
def sort_files_command(*args):
    directory = input("Enter directory path to sort files: ")
    sort_files_in_directory(directory)

#dict for notes menu
NOTES_MENU_COMMANDS = {
    "up": ...,
    "show": display_notes,
    "create": create_note,
    "edit": edit_note,
    "delete": delete_note,
    "add_tag": add_tag_to_note,
    "find_by_tag": find_notes_by_tag,
    "sort_by_tag": sort_notes_by_tag,
    "save": save_note,
    "load": load_note,
    "search": find_note,
}

# function to handle note command
def notes_command(*args):
    completer = CommandCompleter(NOTES_MENU_COMMANDS.keys())
    while True:
        cmd, arguments = user_command_input(completer)
        if cmd == "up":
            break
        elif cmd == "show":
            display_notes(notes)
        else:
            print(execute_commands(NOTES_MENU_COMMANDS, cmd, arguments))
    return "Ok, I return to the main menu."


# dict for main menu handler
MAIN_COMMANDS = {
    "exit": cli_pyassist_exit,
    "sort": sort_files_command,
    "notes": notes_command,
    
}


def execute_commands(menu_commands: dict, cmd: str, arguments: tuple):
    """
    Function to execute user commands

    Args:
        menu_commands (dict): dict for menu-specific commands
        cmd (str): user command
        arguments (tuple): arguments from user input

    Returns:
        func: function with arguments
    """
    if cmd == "sort":
        return sort_files_command(*arguments)
    elif cmd not in menu_commands:
        return f"Command {cmd} is not recognized" + similar_command(cmd, menu_commands.keys())
    cmd = menu_commands[cmd]
    return cmd(*arguments)



@error_handler
def main():
    # completer = CommandCompleter(list(MAIN_COMMANDS.keys()) + list(ADDRESBOOK.keys()))
    completer = CommandCompleter(MAIN_COMMANDS.keys())
    print("Type command or help for command list.")
    while True:
            cmd, arguments = user_command_input(completer)
            print(execute_commands(MAIN_COMMANDS, cmd, arguments))


if __name__ == "__main__":
    main()