import sys
import os
from prompt_toolkit import prompt
from utility.addressbook import AddresBook
from utility.record import Record
from utility.name import Name
from utility.phone import Phone
from utility.email import Email
from utility.birthday import Birthday, FutureDateError
from utility.record_interaction import add_name, create_record

from utility.cmd_complet import CommandCompleter, similar_command

# paths to files with data
ADDRESSBOOK_DATA_PATH = os.path.join(os.getcwd(), "data/addresbook.dat") # Because it's a simple program. The path is hard coded ;)
#ścieżka do pliku z notatkami

#objects storing data while the program is running
ADDRESSBOOK = AddresBook().load_addresbook(ADDRESSBOOK_DATA_PATH)


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
    command = tokens[0]
    arguments = tokens[1:]
    return command, tuple(arguments)



# taking a command from the user
def user_command_input(completer: CommandCompleter):
    user_input = prompt(">>> ", completer=completer).strip().lower()
    if user_input:
        return parse_command(user_input)
    return "", ""
    
# exit / close program
def cli_pyassist_exit(*args):
    ADDRESSBOOK.save_addresbook(ADDRESSBOOK_DATA_PATH)
    # dodać zapisywanie notatek
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
    "add": add_record,
    "up": ...,
}

def addressbook_commands(*args):
    completer = CommandCompleter(ADDRESSBOOK_MENU_COMMANDS.keys())
    while True:
        cmd, arguments = user_command_input(completer)
        if cmd == "up":
            break
        print(execute_commands(ADDRESSBOOK_MENU_COMMANDS, cmd, arguments))
    return "Ok, I return to the main menu."
    

# dict for main menu handler
MAIN_COMMANDS = {
    "exit": cli_pyassist_exit,
    "addressbook": addressbook_commands,
    # "edit": edit_record,
    # "delete / del": delete_record,
    # "show": show_all,
    # "search": search,
    # "save": save_data,
    # "export": export_to_csv,
    # "import": import_from_csv,
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
    if cmd not in menu_commands:
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