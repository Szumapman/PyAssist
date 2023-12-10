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
from utility.notes_interaction import *
from utility.record_interaction import *

from utility.cmd_complet import CommandCompleter, similar_command


# paths to files with data

ADDRESSBOOK_DATA_PATH = os.path.join(os.getcwd(), "data/addresbook.dat") # Because it's a simple program. The path is hard coded ;)



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
    sys.exit("Good bye!")


# @error_handler
def add_record(*args):
    # jeśli użytkownik wpisał po prostu add to zostanie poproszony o podanie nazwy kontaktu do dodania
    if len(args) == 0:
        name = add_name(ADDRESSBOOK)
        
    # jeśli wpisał np. add John Smith to "John Smith" zostanie potraktowane jako nazwa dla nowego kontaku 
    # o ile taki kontakt już nie istnieje
    else:
        name = " ".join(args).strip().title()
        if name in ADDRESSBOOK.keys():
            print(f"Contact {name} already exists. Choose another name.")
            name = add_name(ADDRESSBOOK) 
        else:
            name = Name(name)
    if name is not None:
        record = create_record(name)
        ADDRESSBOOK.add_record(record)
        return f"A record: {record} added to your address book."
    return "Operation cancelled"


# dict for addressbook menu
ADDRESSBOOK_MENU_COMMANDS = {
    "exit": cli_pyassist_exit,
    "add": add_record,
    "edit": lambda *args: edit_record(ADDRESSBOOK, *args),
    "show": lambda *args: show(ADDRESSBOOK, *args),
    "delete": lambda *args: del_record(ADDRESSBOOK, *args),
    "export": lambda *args: export_to_csv(ADDRESSBOOK, *args),
    "import": lambda *args: import_from_csv(ADDRESSBOOK, *args),
    "birthday": lambda *args: show_upcoming_birthday(ADDRESSBOOK, *args),
    "up": ...,
}

def addressbook_commands(*args):
    completer = CommandCompleter(ADDRESSBOOK_MENU_COMMANDS.keys())
    while True:
        cmd, arguments = user_command_input(completer, "address book")
        if cmd == "up":
            break
        print(execute_commands(ADDRESSBOOK_MENU_COMMANDS, cmd, arguments))
    return "Ok, I return to the main menu."
    


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
    "addressbook": addressbook_commands,
    "sort": sort_files_command,
    "notes": notes_command,
    # "edit": edit_record,
    # "show": show_all,
    # "search": search,
    # "save": save_data,
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
