from record import Record

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