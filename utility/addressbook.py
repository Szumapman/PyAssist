import pickle 
import csv
from pathlib import Path
from datetime import datetime, timedelta

from collections import UserDict

from utility.record import Record
from utility.name import Name
from utility.phone import Phone
from utility.email import Email
from utility.birthday import Birthday


class AddresBook(UserDict):
    """
    The AddresBook class extends the UserDict class by adding the add_record method
    and checking that the items added to the dictionary are valid (keys and values based on the Record class).

    Args:
        UserDict (class): parent class
    """

    # function used as a decorator to catch errors when item is adding to addresbook
    def _value_error(func):
        def inner(self, record):
            if not isinstance(record, Record):
                raise ValueError
            return func(self, record)

        return inner

    # Add record to addresbook
    @_value_error
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    # Return all names (keys) from addresbook as formated string
    def show_names(self):
        names = []
        for key in self.keys():
            names.append(key)
        names.sort()
        return "\n".join(names)

    # implementation of the iterator method which returns a generator
    def iterator(self, no_of_contacts_to_return=3):
        if len(self.data) > 0:
            current_record_no = 1
            i = 1
            records_info = ""
            for record in self.values():
                records_info += f"{i}. {record.name}"
                if len(record.phones) > 0:
                    records_info += f"\nphones:{record.show_phones()}"
                if len(record.emails) > 0:
                    records_info += f"\nemails:{record.show_emails()}"
                if record.birthday is not None:
                    records_info += (
                        f"\nbirthday:\n{record.birthday}\n{record.days_to_birthday()}"
                    )
                records_info += "\n-------------\n"
                i += 1
                if current_record_no >= no_of_contacts_to_return:
                    yield records_info
                    current_record_no = 1
                    records_info = ""
                    continue
                current_record_no += 1
            yield records_info  # returns the rest if there are no more records and record_no < no_of_contacts_to_return
        else:
            yield "Nothing to show.\n"

    # method to save addresbook to file
    def save_addresbook(self, filename):
        with open(filename, "wb") as fh:
            pickle.dump(self, fh)
       
    # method to read addresbook from file     
    def load_addresbook(self, filename):
        if Path.exists(Path(filename)):
            with open(filename, "rb") as fh:
                return pickle.load(fh)
        return self
    
    # method to search addresbook
    """
    The method first looks for an exact match in the keys
    then searches the values of the individual records and adds them to the returned Addresbook object if the fragment matches the query.

    Returns:
        Addresbook: a new object of class Addresbook with records based on the query
    """
    def search(self, query: str):
        query_addresbook = AddresBook()
        query = query.strip()
        key_query = query.capitalize()
        if key_query in self.keys():
            query_addresbook[key_query] = self[key_query]
        for record in self.values():
            if query in record.name.value:
                query_addresbook[record.name.value] = record
            for phone in record.phones:
                if query in phone.value:
                    query_addresbook[record.name.value] = record
            for email in record.emails:
                if query in email.value:
                    query_addresbook[record.name.value] = record
            if record.birthday is not None:
                if query in str(record.birthday.value):
                    query_addresbook[record.name.value] = record
        return query_addresbook
            
       
    # export records form addresbook to csv file
    """
    The method exports the data to a csv file. Phones and emails are separated by the '|' char.
    """
    def export_to_csv(self, filename):
        if len(self.data) > 0:
            with open(filename, 'w', newline='') as fh:
                field_names = ['name', 'phones', 'emails', 'birthday']
                writer = csv.DictWriter(fh, fieldnames=field_names)
                writer.writeheader()
                for record in self.data.values():
                    record_dict = {'name': record.name.value}
                    phones = []
                    for phone in record.phones:
                        phones.append(phone.value)
                    record_dict['phones'] = '|'.join(phones)
                    emails = []
                    for email in record.emails:
                        emails.append(email.value)
                    record_dict['emails'] = '|'.join(emails)
                    if record.birthday is not None:
                        record_dict['birthday'] = record.birthday.value.strftime("%d %m %Y")
                    writer.writerow(record_dict)
                
                    
    # import from csv file
    """
    The method imports data into a csv file. 
    
    Data structures in the file:
    name,phones,emails,birthsday
    
    Phones and emails are separated (if there is more than one phone or email) with "|".
    Birthday should be written as: day month year e.g. 21 12 1999 or 30-01-2012 or 09/01/1987
    """
    def import_from_csv(self, filename):
        with open(filename, 'r', newline='') as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                name = row['name']
                phones = row['phones'].split('|')
                phones_to_add = []
                for phone in phones:
                    if phone != '':
                        phones_to_add.append(Phone(phone))
                emails = row['emails'].split('|')
                emails_to_add = []
                for email in emails:
                    if email != '':
                        emails_to_add.append(Email(email))
                birthday = row['birthday']
                if birthday != '':
                    birthday = Birthday(birthday)
                else:
                    birthday = None    
                self.add_record(Record(Name(name), phones_to_add, emails_to_add, birthday))
                

    def records_with_upcoming_birthday(self) -> dict:
        """
        The function return a dict which the keys are the days of the week from current day and next 7 days as a datetime.date(), 
        and the values are lists with Records having birthdays on a given day.

        Returns:
            dict: key datetime.date from today + next 7 days, values lists of Records with birthdays in corresponding day
        """
        current_date = datetime.now().date()
        this_week_birthdays = {current_date + timedelta(days=i): [] for i in range(8)}
        for record in self.values():
            if record.birthday is not None:
                this_year_birthday = datetime(year=current_date.year, month=record.birthday.value.month, day=record.birthday.value.day).date()
                difference = (this_year_birthday - current_date).days
                if -1 < difference < 8:
                    this_week_birthdays[current_date + timedelta(difference)].append(record)
        return this_week_birthdays


    # Returns a formatted string of birthdays
    def show_birthdays(self, upcoming_birthdays_dict=None):
        """
        Display birthdays for each date in the provided dictionary.

        Args:
            birthdays_dict (dict): Dictionary with dates as keys and lists of records as values.
        """
        birthdays_str = ""
        for date, records in upcoming_birthdays_dict.items():
            birthdays_str += f"Birthdays on {date}:\n"
            if not records:
                birthdays_str += "  Nobody\n"
            else:
                for record in records:
                    name = record.name.value if record.name else None
                    birthdays_str += f"  {name}\n" if name else ""
        return birthdays_str or "No birthdays in the next 7 days."                 