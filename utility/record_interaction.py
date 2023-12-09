from .record import Record
from .phone import Phone
from .name import Name


# function to handle with errors
def error_handler(func):
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


def create_record(name):
    phones = []
    emails = []
    # birthday = None
    # address = None
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