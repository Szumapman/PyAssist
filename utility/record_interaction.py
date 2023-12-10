from .record import Record
from .phone import Phone
from .email import Email
from .birthday import Birthday
from .address import Address
from .name import Name
from utility.addressbook import AddresBook
import os

from prompt_toolkit import prompt
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
            # except FutureDateError:
            #     print("You can't use a future date as a birthday, try again.")
            except FileNotFoundError:
                print("I can't find file to import data.")
                break
    return wrapper


@error_handler
def add_name(addressbook) -> Name:
    while True:
        name = input("Type name or <<< if you want to cancel: ").strip().title()
        if name in addressbook.keys():
            print(f"Contact {name} already exists. Choose another name.")
            continue
        elif name == "<<<":
            return None
        return Name(name)


@error_handler
def add_phone():
    phone = input("Type phone or <<< if you want to cancel: ")
    if phone == "<<<":
        return None
    return Phone(phone)


@error_handler
def add_email():
    email = input("Type email or <<< if you want to cancel: ")
    if email == "<<<":
        return None
    return Email(email)


@error_handler
def add_birthday():
    birthday = input("Input the date of birth as day month year (e.g. 15-10-1985 or 15 10 1985) or <<< if you want to cancel: ")
    if birthday == "<<<":
        return None
    return Birthday(birthday)    
    

#@error_handler
def add_address():
    street = input("street: ")
    city = input("city: ")
    zip_code = input("zip code: ")
    country = input("country: ")
    return Address(street, city, zip_code, country)

def create_record(name):
    phones = []
    emails = []
    birthday = None
    address = None
    while True:
        answer = (input("Type Y (yes) if you want to add phone number: ").strip().lower())
        if answer == "y" or answer == "yes":
            while True:
                phone = add_phone()
                if phone is not None:
                    phones.append(phone)
                    answer = (input("Type Y (yes) if you want to add another phone number: ").strip().lower())
                    if answer == "y" or answer == "yes":
                        continue
                break
        break
    
    while True:
        answer = input("Type Y (yes) if you want to add email: ").strip().lower()
        if answer == "y" or answer == "yes":
            while True:
                email = add_email()
                if email is not None:
                    emails.append(email)
                    answer = (input("Type Y (yes) if you want to add another email: ").strip().upper())
                    if answer == "y" or answer == "yes":
                        continue
                break
        break
    
    answer = input("Type Y (yes) if you want to add birthday: ").strip().lower()
    if answer == "y" or answer == "yes":
        birthday = add_birthday()
    
    answer = input("Type Y (yes) if you want to add address: ").strip().lower()
    if answer == "y" or answer == "yes":
        address = add_address()
    
    return Record(name, phones, emails, birthday, address)

#####################################
# edit existing name
def edit_name(addressbook, *args):
    while True:
        name = " ".join(args).strip().title()
        print(f"Type new name for contact {name}")
        new_name = input("New name: ").strip().title()

        if not new_name:
            print("Name cannot be empty. Please try again.")
            continue

        if new_name == name:
            print("The new name is the same as the current name. Please provide a different name.")
            continue

        if new_name in ADDRESSBOOK.keys():
            print("A contact with this name already exists. Please choose a different name.")
            continue

        addressbook[new_name] = Record(new_name, addressbook.phones, addressbook.emails, addressbook.birthday, addressbook.address)
        del addressbook[addressbook.name.value]
        break

# # init function for phone changed
# @error_handler
# def edit_phone(addresbook, record):
#     change_data(record, "phone")

# # init function for email changed
# @error_handler
# def edit_email(addresbook, record):
#     change_data(record, "email")
    
# # changing birthday
# @error_handler
# def edit_birthday(addresbook, record):
#     birthday = add_birthday()
#     addresbook[record.name.value].birthday = birthday

# @error_handler
# def edit_address(existing_address):
#     if existing_address:
#         street = input(f"Enter the new street (press Enter to keep the current street - {existing_address.street}): ")
#         city = input(f"Enter the new city (press Enter to keep the current city - {existing_address.city}): ")
#         zip_code = input(f"Enter the new zip code (press Enter to keep the current zip code - {existing_address.zip_code}): ")
#         country = input(f"Enter the new country (press Enter to keep the current country - {existing_address.country}): ")

#         return Address(street or existing_address.street,
#                        city or existing_address.city,
#                        zip_code or existing_address.zip_code,
#                        country or existing_address.country)
#     else:
#         # If existing_address is None, create a new Address object
#         street = input("Enter the street: ")
#         city = input("Enter the city: ")
#         zip_code = input("Enter the zip code: ")
#         country = input("Enter the country: ")

#         if street or city or zip_code or country:
#             return Address(street, city, zip_code, country)
#         else:
#             return None

# # help menu function to choose email or phone
# def item_selection(record, data_list, show):
#     print(f"Contact {record.name} {type}s:\n{show}", end="")
#     number_to_change = input("Select by typing a number (for example 1 or 2): ")
#     try:
#         number_to_change = int(number_to_change) - 1
#         if number_to_change >= len(data_list) or number_to_change < 0:
#             raise ValueError
#         return number_to_change
#     except ValueError:
#         return -1
    
# # change of phone or email
# def change_data(record, type):
#     if type == "phone":
#         data_list = record.phones
#         show = record.show_phones()
#         add_type = record.add_phone
#     elif type == "email":
#         data_list = record.emails
#         show = record.show_emails()
#         add_type = record.add_email
#     while True:
#         if len(data_list) > 0:
#             while True:
#                 answer = input(
#                     f"Contact {record.name} {type}s:{show}\nDo you want change it or add another? 1 chanege, 2 add, 3 delete: "
#                 )
#                 if answer == "1":
#                     if len(data_list) == 1:
#                         data_to_add = add_email() if type == "email" else add_phone()
#                         if data_to_add is not None:
#                             data_list[0] = data_to_add
#                         break
#                     else:
#                         number_to_change = item_selection(record, data_list, show)
#                         if number_to_change == -1:
#                             print("Wrong option, try again")
#                             break
#                         data_to_add = add_email() if type == "email" else add_phone()
#                         if data_to_add is not None:
#                             data_list[number_to_change] = data_to_add
#                         break
#                 elif answer == "2":
#                     data_to_add = add_email() if type == "email" else add_phone()
#                     if data_to_add is not None:
#                         add_type(data_to_add)
#                     break
#                 elif answer == "3":
#                     if len(data_list) == 1:
#                         data_list.clear()
#                         break
#                     else:
#                         number_to_delete = item_selection(record, data_list, show)
#                         if number_to_delete == -1:
#                             print("Wrong option, try again")
#                             break
#                         print(
#                             f"{type} no {number_to_delete+1}: {data_list.pop(number_to_delete)} deleted."
#                         )
#                         break
#                 else:
#                     print("Unrecognized command, try again.")
#         else:
#             add_type(add_email() if type == "email" else add_phone())
#         break


# dict for menu edit handler
EDIT_COMMANDS = {
    "name": lambda *args: edit_name(ADDRESSBOOK, *args), 
    #"phone": edit_phone, 
    #"email": edit_email,
    #"address": edit_address,
    #"birthday": edit_birthday,
    "up": ...,
    }

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

def edit_commands(addressbook, *args):
    completer = CommandCompleter(EDIT_COMMANDS.keys())
    while True:
        cmd, arguments = user_command_input(completer)
        if cmd == "up":
            break
        print(execute_commands(EDIT_COMMANDS, cmd, arguments))
    return "Ok, I return to the addressbook menu."

################################################
# record edit
def edit_record(addressbook, *args):
    if not args:
        name = input("Enter the name of the record you want to edit: ").strip().title()
    else:
        name = " ".join(args).strip().title()

    if name in addressbook:
        print("Enter what you want to edit: ")
        edit_commands(ADDRESSBOOK, *args)
        return f"Record {name} changed successfully."
    else:
        return f"Record {name} not found in the address book."