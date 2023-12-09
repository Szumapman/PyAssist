import sys
import os
from typing import Callable
from prompt_toolkit import prompt
from utility.addressbook import AddresBook
from utility.record import Record
from utility.name import Name
from utility.phone import Phone
from utility.email import Email
from utility.birthday import Birthday, FutureDateError

from utility.cmd_complet import CommandCompleter, similar_command

# paths to files with data
ADDRESBOOK_DATA_PATH = os.path.join(os.getcwd(), "data/addresbook.dat") # Because it's a simple program. The path is hard coded ;)
#ścieżka do pliku z notatkami

#objects storing data while the program is running
ADDRESBOOK = AddresBook().load_addresbook(ADDRESBOOK_DATA_PATH)


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



# exit / close program
def cli_pyassist_exit(*args):
    ADDRESBOOK.save_addresbook(ADDRESBOOK_DATA_PATH)
    # dodać zapisywanie notatek
    print("Your data has been saved.") 
    sys.exit("Good bye!")

    
# hendler for main menu
def get_main_handler(command):
    return MAIN_COMMANDS[command]

   
# dict for main menu handler
MAIN_COMMANDS = {
    "exit": cli_pyassist_exit,
    "addals": cli_pyassist_exit,
    "addall": cli_pyassist_exit,
    "edit": cli_pyassist_exit,
    "delete / del": cli_pyassist_exit,
    "show": cli_pyassist_exit,
    "search": cli_pyassist_exit,
    "save": cli_pyassist_exit,
    "export": cli_pyassist_exit,
    "import": cli_pyassist_exit,
}


# def similar_command(cmd):
#     for key in MAIN_COMMANDS:
#         if cmd in key or key in cmd:
#            return  f"\nmaybe you meant: {key}"



def execute_commands(cmd, arguments):
    """
    Function to execute user commands

    Args:
        cmd (str): user command
        arguments (tuple): arguments from user input

    Returns:
        func: function with arguments
    """
    if cmd not in MAIN_COMMANDS:
        return f"Command {cmd} is not recognized" + similar_command(cmd, MAIN_COMMANDS.keys())
    cmd = MAIN_COMMANDS[cmd]
    return cmd(*arguments)



@error_handler
def main():
    completer = CommandCompleter(list(MAIN_COMMANDS.keys()) + list(ADDRESBOOK.keys()))
    print("Type command or help for command list.")
    while True:
        user_input = prompt(">>> ", completer=completer).strip().lower()
        if user_input:
            cmd, arguments = parse_command(user_input)
            print(execute_commands(cmd, arguments))


if __name__ == "__main__":
    main()