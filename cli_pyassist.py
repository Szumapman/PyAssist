import sys
import os
import csv
import pyfiglet
import cowsay
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
from utility.notes_interaction import *
from utility.record_interaction import *

from utility.cmd_complet import CommandCompleter, similar_command


# paths to files with data # Because it's a simple program. The path is hard coded ;)
current_dir = os.path.dirname(os.path.abspath(__file__))
NOTES_DATA_PATH = os.path.join(current_dir, "data/notes.csv")
ADDRESSBOOK_DATA_PATH = os.path.join(current_dir, "data/addresbook.dat") 


#objects storing data while the program is running
ADDRESSBOOK = AddresBook().load_addresbook(ADDRESSBOOK_DATA_PATH)


#initialize an instance of FileSorter class
file_sorter = FileSorter()

#function for FileSorter in specified directory
def sort_files_in_directory(directory):
    file_sorter.process_folder(directory)
    
# function to handle sort command
def sort_files_command(*args):
    directory = input("Enter directory path to sort files: ")
    sort_files_in_directory(directory)
    return f"Done."

# function to handle with errors
def error_handler(func):
    def wrapper(*args):
        while True:
            try:
                return func(*args)
            # błędy i komunikaty przeniesione z pierwotnej wersji - do sprawdzenia / zmiany
            except ValueError:
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
    command = tokens[0].lower()
    arguments = tokens[1:]
    return command, tuple(arguments)

# taking a command from the user
def user_command_input(completer: CommandCompleter):
    user_input = prompt(">>> ", completer=completer).strip().lower()
    if user_input:
        return parse_command(user_input)

# taking a command from the user
def user_command_input(completer: CommandCompleter, menu_name=""):
    user_input = prompt(f"{menu_name} >>> ", completer=completer).strip()
    if user_input:
        return parse_command(user_input)
    return "", ""
    
# exit / close program
def cli_pyassist_exit(*args):
    Note.save_notes(notes, NOTES_DATA_PATH)   
    ADDRESSBOOK.save_addresbook(ADDRESSBOOK_DATA_PATH)
    print("Your data has been saved.")
    cowsay.tux("Good bye!") 
    sys.exit()

# function to handle addressbook command
def addressbook_commands(*args):
    menu_options = [
        {"option": "Show All Records", "command": "show"},
        {"option": "Show Specific Record", "command": "show <name>"},
        {"option": "Add Record", "command": "add"},
        {"option": "Edit Record", "command": "edit"},
        {"option": "Delete Record", "command": "delete"},
        {"option": "Search in Addressbook", "command": "search <query>"},
        {"option": "Upcoming Birthdays", "command": "birthday <days>"}, # (selected number of days ahead) - informacja do instrukcji 
        {"option": "Export Address Book", "command": "export"},
        {"option": "Import Address Book", "command": "import"},
        {"option": "Show this Menu", "command": "help"},
        {"option": "Main Menu", "command": "up"},
    ]

    max_option_length = max(len(item['option']) for item in menu_options) 
    
    print("Options:".ljust(max_option_length + 5), "Command:")
    print("-" * (max_option_length + 18))

    for index, item in enumerate(menu_options):
        print(f"{item['option'].ljust(max_option_length + 5)} {item['command']}")

    print("-" * (max_option_length + 18))
    completer = CommandCompleter(list(ADDRESSBOOK_MENU_COMMANDS.keys()) + list(ADDRESSBOOK.keys()))
    while True:
        cmd, arguments = user_command_input(completer, "address book")
        if cmd == "up":
            break
        print(execute_commands(ADDRESSBOOK_MENU_COMMANDS, cmd, arguments))
    return "Ok, I return to the main menu."

# function to handle note command
def notes_command(*args):
    menu_options = [
        {"option": "Show Notes", "command": "show"},
        {"option": "Search Note", "command": "search"},
        {"option": "Create Note", "command": "create"},
        {"option": "Edit Note", "command": "edit"},
        {"option": "Delete Note", "command": "delete"},
        {"option": "Add Tag to Note", "command": "addtag"},
        {"option": "Find Notes by Tag", "command": "findtag"},
        {"option": "Sort Notes by Tag", "command": "sorttag"},
        {"option": "Export Notes", "command": "export"},
        {"option": "Import Notes", "command": "import"},
        {"option": "Show this Menu", "command": "help"},
        {"option": "Main Menu", "command": "up"}
    ]

    max_option_length = max(len(item['option']) for item in menu_options) 
    
    print("Options:".ljust(max_option_length + 5), "Command:")
    print("-" * (max_option_length + 15))

    for index, item in enumerate(menu_options):
        print(f"{item['option'].ljust(max_option_length + 5)} {item['command']}")

    print("-" * (max_option_length + 15))
    completer = CommandCompleter(NOTES_MENU_COMMANDS.keys())
    while True:
        cmd, arguments = user_command_input(completer, "notes")
        if cmd == "up":
            break
        elif cmd == "show":
            display_notes(notes)
        else:
            print(execute_commands(NOTES_MENU_COMMANDS, cmd, arguments))
    return "Ok, I return to the main menu."

# dict for addressbook menu
ADDRESSBOOK_MENU_COMMANDS = {
    "exit": cli_pyassist_exit,
    "add": lambda *args: add_record(ADDRESSBOOK, *args),
    "edit": lambda *args: edit_record(ADDRESSBOOK, *args),
    "show": lambda *args: show(ADDRESSBOOK, *args),
    "delete": lambda *args: del_record(ADDRESSBOOK, *args),
    "export": lambda *args: export_to_csv(ADDRESSBOOK, *args),
    "import": lambda *args: import_from_csv(ADDRESSBOOK, *args),
    "birthday": lambda *args: show_upcoming_birthday(ADDRESSBOOK, *args),
    "search": lambda *args: search(ADDRESSBOOK, *args),
    "up": ...,
    "help": addressbook_commands,
}

#dict for notes menu
NOTES_MENU_COMMANDS = {
    "up": ...,
    "show": display_notes,
    "create": create_note,
    "edit": edit_note,
    "delete": delete_note,
    "addtag": add_tag_to_note,
    "findtag": find_notes_by_tag,
    "sorttag": sort_notes_by_tag,
    "export": save_note,
    "import": load_note,
    "search": find_note,
    "help": notes_command
}


# dict for main menu handler
MAIN_COMMANDS = {
    "exit": cli_pyassist_exit,
    "addressbook": addressbook_commands,
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
    logo = pyfiglet.figlet_format("PyAssist", font = "slant")
    print(logo)
    print("     ╔════════════════════════════╗")
    print("     ║         Main Menu          ║")
    print("     ╠════════════════════════════╣")
    print("     ║ - addressbook              ║")
    print("     ║ - notes                    ║")
    print("     ║ - sorter                   ║")
    print("     ║ - exit                     ║")
    print("     ╚════════════════════════════╝")
    while True:
            cmd, arguments = user_command_input(completer)
            print(execute_commands(MAIN_COMMANDS, cmd, arguments))


if __name__ == "__main__":
    main()
