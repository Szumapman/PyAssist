# PyAssist

> Krótki opis projektu PL
>
> Short project description EN
> PyAssist is a Python-based command-line utility designed to assist you in managing your address book and notes efficiently. With PyAssist, you can easily add, edit, delete, search, and export records in your address book. Additionally, you can create, edit, delete, and search notes with various functionalities.
> Live demo [_here_](https://www.example.com). <!-- If you have the project hosted somewhere, include the link here. -->

## Język / Language

- [Polski / Polish](#spis-treści)
- [Angielski / English](#table-of-contents)

## Spis treści

- [Informacje ogólne](#informacje-ogólne)
- [Konfiguracja](#konfiguracja)
- [Instalacja](#instalacja)
- [Uruchomienie programu](#uruchomienie-programu)
- [Funkcje](#funkcje)
- [Przykłady użycia](#przykłady-użycia)
- [Licencja](#licencja)
- [Autorzy](#autorzy)
- [Kontakt](#kontakt)

## Informacje ogólne

- Podaj tutaj ogólne informacje o swoim projekcie.
- Jaki problem rozwiązuje (zamierza rozwiązać)?
- Jaki jest cel twojego projektu?
- Dlaczego się go podjąłeś?
<!-- Nie musisz odpowiadać na wszystkie pytania - tylko na te, które są istotne dla Twojego projektu. -->

## Konfiguracja

Np. Przed uruchomieniem aplikacji, upewnij się, że na Twoim komputerze zainstalowany jest Python w wersji 3.x.

## Instalacja

## Uruchomienie programu

## Funkcje

## Przykłady użycia

Jak można z niego korzystać?
Podajemy tutaj różne przypadki użycia i przykłady kodu.

## Licencja

## Autorzy

## Kontakt

Stworzony przez:

- XXX

## Table of Contents

- [General Information](#general-information)
- [Setup](#setup)
- [Installation](#installation)
- [Running the application](#running-the-application)
- [Functions](#functions)
- [Examples of use](#example-of-use)
- [Licence](#licence)
- [Authors](#authors)
- [Contact](#contact)

## General Information

### Problem Statement

The project addresses the challenge of organizing and managing contact information effectively. Traditional methods of managing contacts and notes can be cumbersome, and PyAssist aims to provide a streamlined and efficient solution.

### Project Goals

The primary goals of PyAssist include:

- Simplifying the process of managing address book records.
- Providing a convenient and powerful tool for note-taking and organization.
- Offering functionalities for sorting files in a specified directory.

### Motivation

The motivation behind the project stems from the need for a versatile and user-friendly command-line tool for personal information management. PyAssist was developed to offer an intuitive interface for handling contacts and notes, allowing users to focus on productivity rather than dealing with cumbersome organizational tasks.

### Voice Search Functionality

PyAssist introduces a cutting-edge voice search feature, allowing users to interact with the tool through spoken commands. This innovative functionality enhances the user experience by enabling hands-free operation, particularly useful for users on the go or those who prefer voice commands.

#### To utilize the voice search feature:

1. Simply speak your command after entering the designated voice search mode.
2. PyAssist will process your spoken command and execute the corresponding action.

This feature adds a new dimension to the user interface, making PyAssist even more accessible and user-friendly.

### Main Menu

Upon launching PyAssist, you'll be greeted with the main menu, where you can choose from the following options:

- `addressbook`: Access the address book management menu.
- `notes`: Access the notes management menu.
- `sort`: Sort files in a specified directory.
- `exit`: Exit PyAssist.

### Address Book Menu

In the address book menu, you can perform the following actions:

- `add`: Add a new record to the address book.
- `edit`: Edit an existing record in the address book.
- `show`: Display all records or a specific record in the address book.
- `delete`: Delete a record from the address book.
- `export`: Export the address book to a CSV file.
- `import`: Import data from a CSV file to the address book.
- `birthday`: View upcoming birthdays within a specified number of days.
- `search`: Search for a specific record in the address book.

### Notes Menu

In the notes menu, you can manage your notes:

- `show`: Display all notes.
- `search`: Search for a specific note.
- `create`: Create a new note.
- `edit`: Edit an existing note.
- `delete`: Delete a note.
- `addtag`: Add a tag to a note.
- `findtag`: Find notes by a specific tag.
- `sorttag`: Sort notes by tag.
- `export`: Export notes to a file.
- `import`: Import notes from a file.

### Sort Files

PyAssist allows you to sort files in a specified directory. Simply choose the "sort" option from the main menu, and follow the prompts to enter the directory path.

### Exit

To exit PyAssist and save your data, choose the "exit" option from the main menu.

### Project Structure

The PyAssist project is structured as follows:

- `pyassist.py`: The main script that initializes and runs the PyAssist application.
- `utility`: A directory containing various utility modules used by PyAssist.
- `addressbook.py`: Defines the AddressBook class for managing address book records.
- `record.py`: Defines the Record class for storing individual records.
- `name.py`: Defines the Name class for handling names.
- `phone.py`: Defines the Phone class for handling phone numbers.
- `email.py`: Defines the Email class for handling email addresses.
- `birthday.py`: Defines the Birthday class for handling birthdays.
- `notes.py`: Defines the Note class for managing notes.
- `sorter.py`: Defines the FileSorter class for sorting files in a directory.
- `notes_interaction.py`: Contains functions for interacting with notes.
- `record_interaction.py`: Contains functions for interacting with address book records.
- `cmd_complet.py`: Defines the CommandCompleter class for command-line auto-completion.

## Setup

## Installation

## Running the application

## Functions

In the PyAssist code, several key functions enable interactive management of data in an organized manner. Here's a brief description of the main functions included in the code:

### 1. Adding, Editing, and Deleting Contacts (Addressbook)

#### Function `add_record(record: Record)` in the `AddressBook` class:

Adds a new contact to the address book. It checks whether the added object is an instance of the `Record` class, ensuring the correctness of contact data.

#### Function `edit_record(ADDRESSBOOK, *args)` in the `Record` class:

Allows editing an existing contact in the address book, enabling changes to data such as phone numbers, email addresses, etc.

#### Function `del_record(ADDRESSBOOK, *args)` in the `Record` class:

Deletes a contact from the address book.

### 2. Displaying and Searching Contacts

#### Function `show_names()` in the `AddressBook` class:

Returns a formatted string containing all names (keys) in the address book.

#### Function `iterator(no_of_contacts_to_return=3)` in the `AddressBook` class:

Iterates through records and returns formatted information in groups of a specified size, facilitating contact browsing.

#### Function `search(query: str)` in the `AddressBook` class:

Searches for contacts in the address book based on the given query and returns a new `AddressBook` class object matching the query.

### 3. Managing Notes

Functions in the `NotesMenuCommands` class (`notes.py`): Allow displaying, creating, editing, deleting, adding tags, searching, and sorting notes.

### 4. File Sorting Function

#### Function `sort_files_command(*args)` in the main code:

Sorts files in a specified directory, which can be useful for organizing data on disk.

### 5. Voice Search Functionality

Functions in the main code: Introduced an innovative voice search feature, allowing users to interact with the tool using voice commands. By enabling voice search mode, users can issue commands via speech.

### 6. Export and Import Functions

#### Functions `export_to_csv(filename: str)` and `import_from_csv(filename: str)` in the `AddressBook` class:

Allow exporting and importing contact data to and from CSV files.

### 7. Error Handling

Decorator `@error_handler` in the main code: Provides error handling during adding, editing, exporting, and other operations, improving the program's reliability.

The integrated usage examples in the README section allow for a quick understanding of how to use individual PyAssist functions.

## Examples of use

### Adding a New Contact to the Address Book

<!-- sc -->

### Searching for a Contact by Name

<!-- sc -->

### Creating a New Note

<!-- sc -->

### Using Voice Search

<!-- sc -->

## Licence

## Authors

## Contact
