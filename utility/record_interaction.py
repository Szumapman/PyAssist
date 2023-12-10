from .record import Record
from .phone import Phone
from .email import Email
from .birthday import Birthday
from .address import Address
from .name import Name


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

def del_record(addressbook, *args):
    if not args:
        name = input("Enter the name of the record you want to delete: ").strip().title()
    else:
        name = " ".join(args).strip().title()

    if name in addressbook:
        del addressbook[name]
        return f"Record {name} deleted successfully."
    else:
        return f"Record {name} not found in the address book."
    
def export_to_csv(addressbook) -> None:
    while True:
        filename = input("Type the filename to export to (e.g., output.csv) or <<< to cancel: ").strip()
        

def show(addressbook, *args):
    if len(args) == 1:
        if args[0] == "all":
            for info in addressbook.iterator():
                print(info, end="")
                if info != "":
                    input("Press Enter to continue. ")
            return "" 
        name_record_to_show = " ".join(args).strip().title()
        if name_record_to_show in addressbook:
            return f"{addressbook[name_record_to_show]}"
        return f"Contact {name_record_to_show} doesn't exist."
        if filename == "<<<" or filename == "":
            return "Export cancelled."
        

        try:
            addressbook.export_to_csv(filename)
            return f"Data exported successfully to {filename}."
        except FileNotFoundError:
            return "Error: Unable to find the specified file. Please try again."
        except Exception as e:
            return f"Error: {e}. Please try again."
            
def import_from_csv(addressbook):
    filename = input("Enter the CSV file name for import: ").strip()
    if filename == "<<<" or filename == "":
            return "Import cancelled."
   
    
    try:
        addressbook.import_from_csv(filename)
        return f"Data imported successfully from {filename}."
    except FileNotFoundError:
            return "Error: Unable to find the specified file. Please try again."
    except Exception as e:
            return f"Error: {e}. Please try again."