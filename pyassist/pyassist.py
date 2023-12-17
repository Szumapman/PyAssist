import sys
from pathlib import Path
import pyfiglet
import cowsay
from prompt_toolkit import prompt
from utility.addressbook import AddresBook
from utility.notes import Note
from utility.sorter import FileSorter
from utility.notes_interaction import *
from utility.record_interaction import *
from utility.cmd_complet import CommandCompleter, similar_command


# paths to files with data # Because it's a simple program. The path is hard coded ;)
program_dir = Path(__file__).parent
NOTES_DATA_PATH = program_dir.joinpath('data/notes.csv')
ADDRESSBOOK_DATA_PATH = program_dir.joinpath("data/addresbook.dat") 


#objects storing data while the program is running
NOTES = Note.load_notes(NOTES_DATA_PATH)
ADDRESSBOOK = AddresBook().load_addresbook(ADDRESSBOOK_DATA_PATH)
    

# function to handle with errors
def error_handler(func):
    def wrapper(*args):
        while True:
            try:
                return func(*args)
            except FileNotFoundError as e: 
                return f"I can't find folder."
            except KeyboardInterrupt:
                cli_pyassist_exit()
    return wrapper


# function to handle sort command
@error_handler
def sort_files_command(*args):
    if not args:
        directory = input("Enter directory path to sort files: ")
    else:
        directory = "".join(args)
    file_sorter = FileSorter()
    file_sorter.process_folder(directory)
    return f"Done."


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
def user_command_input(completer: CommandCompleter, menu_name=""):
    user_input = prompt(f"{menu_name} >>> ", completer=completer).strip()
    if user_input:
        return parse_command(user_input)
    return "", ""
    
# exit / close program
def cli_pyassist_exit(*args):
    Note.save_notes(NOTES, NOTES_DATA_PATH)   
    ADDRESSBOOK.save_addresbook(ADDRESSBOOK_DATA_PATH)
    cowsay.tux("Your data has been saved.\nGood bye!") 
    sys.exit()


# function to show menus addressbook & notes
def show_menu(menu_options):
    max_option_length = max(len(item['option']) for item in menu_options) 
    print("Options:".ljust(max_option_length + 5), "Command:")
    print("-" * (max_option_length + 24))
    for _, item in enumerate(menu_options):
        print(f"{item['option'].ljust(max_option_length + 5)} {item['command']}")
    print("-" * (max_option_length + 24))


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
        {"option": "Main Menu", "command": "up"}, 
        {"option": "Program exit", "command": "exit"},
        {"option": "Show this Menu", "command": "help"},
    ]
    show_menu(menu_options)
    completer = CommandCompleter(list(ADDRESSBOOK_MENU_COMMANDS.keys()) + list(ADDRESSBOOK.keys()))
    while True:
        cmd, arguments = user_command_input(completer, "address book")
        print(execute_commands(ADDRESSBOOK_MENU_COMMANDS, cmd, ADDRESSBOOK, arguments))


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
        # {"option": "Export Notes", "command": "export"},
        # {"option": "Import Notes", "command": "import"},
        {"option": "Main Menu", "command": "up"},
        {"option": "Program exit", "command": "exit"},
        {"option": "Show this Menu", "command": "help"},
    ]
    show_menu(menu_options)
    completer = CommandCompleter(NOTES_MENU_COMMANDS.keys())
    while True:
        cmd, arguments = user_command_input(completer, "notes")
        print(execute_commands(NOTES_MENU_COMMANDS, cmd, NOTES, arguments))


# dict for main menu handler
MAIN_COMMANDS = {
    "exit": cli_pyassist_exit,
    "addressbook": addressbook_commands,
    "sort": sort_files_command,
    "notes": notes_command,
}


@error_handler
def pyassit_main_menu(*args):
    menu_options = [
        {"option": "Open your address book", "command": "addressbook"},
        {"option": "Open your notes", "command": "notes"},
        {"option": "Sort files in <directory>", "command": "sort <directory>"}, 
        {"option": "Program exit", "command": "exit"},
        {"option": "Show this Menu", "command": "help"},
    ]
    show_menu(menu_options)
    completer = CommandCompleter(MAIN_COMMANDS.keys())
    while True:
        cmd, arguments = user_command_input(completer, "main menu")
        print(execute_commands(MAIN_COMMANDS, cmd, None, arguments))

# dict for addressbook menu
ADDRESSBOOK_MENU_COMMANDS = {
    "exit": cli_pyassist_exit,
    "add": add_record, #lambda *args: add_record(ADDRESSBOOK, *args),
    "edit": edit_record, #lambda *args: edit_record(ADDRESSBOOK, *args),
    "show": show, #lambda *args: show(ADDRESSBOOK, *args),
    "delete": del_record, #lambda *args: del_record(ADDRESSBOOK, *args),
    "export": export_to_csv, #lambda *args: export_to_csv(ADDRESSBOOK, *args),
    "import": import_from_csv, #lambda *args: import_from_csv(ADDRESSBOOK, *args),
    "birthday": show_upcoming_birthday, #lambda *args: show_upcoming_birthday(ADDRESSBOOK, *args),
    "search": search, #lambda *args: search(ADDRESSBOOK, *args),
    "up": pyassit_main_menu,
    "help": addressbook_commands,
}

#dict for notes menu
NOTES_MENU_COMMANDS = {
    "show": show_notes, #lambda *args: show_notes(NOTES, *args),
    "create": create_note, #lambda *args: create_note(NOTES, *args),
    "edit": edit_note, #lambda *args: edit_note(NOTES, *args),
    "delete": delete_note, #lambda *args: delete_note(NOTES, *args),
    "addtag": add_tag_to_note, #lambda *args: add_tag_to_note(NOTES, *args),
    "findtag": find_notes_by_tag, #lambda *args: find_notes_by_tag(NOTES, *args),
    "sorttag": sort_notes_by_tag, #lambda *args: sort_notes_by_tag(NOTES, *args),
    # "export": save_note,
    # "import": load_note,
    "search": show_search, #lambda *args: show_search(NOTES, *args),
    "up": pyassit_main_menu,
    "exit": cli_pyassist_exit, 
}
    
    
def execute_commands(menu_commands: dict, cmd: str, data_to_use, arguments: tuple):
    """Function to execute user commands

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
    return cmd(data_to_use, *arguments)


def main():
    print(pyfiglet.figlet_format("PyAssist", font = "slant"))
    # print("     ╔════════════════════════════╗")
    # print("     ║         Main Menu          ║")
    # print("     ╠════════════════════════════╣")
    # print("     ║ - addressbook              ║")
    # print("     ║ - notes                    ║")
    # print("     ║ - sort                     ║")
    # print("     ║ - exit                     ║")
    # print("     ╚════════════════════════════╝")
    pyassit_main_menu()
    

if __name__ == "__main__":
    main()