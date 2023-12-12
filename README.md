# PyAssist

> PyAssist to narzędzie wiersza poleceń oparte na języku Python, które zostało zaprojektowane w celu efektywnego zarządzania książką adresową i notatkami. Dzięki PyAssist możesz łatwo dodawać, edytować, usuwać, wyszukiwać i eksportować rekordy w swojej książce adresowej. Dodatkowo, narzędzie umożliwia tworzenie, edytowanie, usuwanie i wyszukiwanie notatek, oferując różnorodne funkcje.

> PyAssist is a Python-based command-line utility designed to assist you in managing your address book and notes efficiently. With PyAssist, you can easily add, edit, delete, search, and export records in your address book. Additionally, you can create, edit, delete, and search notes with various functionalities.


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

### Zdefiniowanie problemu rozwiązywanego przez Pyassist

Projekt rozwiązuje problem związany z efektywnym organizowaniem i zarządzaniem informacjami z książki adresowej, a także notatkami. Tradycyjne metody korzystania z kontaktów i notatek mogą być uciążliwe, a PyAssist ma na celu dostarczenie zoptymalizowanego i efektywnego rozwiązania.

### Cele projektu

Główne cele PyAssist obejmują:

1. Uproszczenie procesu zarządzania rekordami książki adresowej.
2. Dostarczenie wygodnego i potężnego narzędzia do robienia notatek oraz organizacji.
3. Oferowanie funkcji sortowania plików w określonym katalogu.

### Potrzeba stworzenia projektu

Potrzeba stworzenia tego projektu wynika z potrzeby wszechstronnego i przyjaznego użytkownikowi narzędzia wiersza poleceń do zarządzania informacjami osobistymi. PyAssist został stworzony, aby zapewnić intuicyjny interfejs obsługi kontaktów i notatek, pozwalając użytkownikom skupić się na produktywności, zamiast zajmować się uciążliwymi zadaniami organizacyjnymi.

### Funkcjonalność głosowego wyszukiwania

PyAssist wprowadza innowacyjną funkcję głosowego wyszukiwania, umożliwiającą interakcję z narzędziem za pomocą komend głosowych. Ta innowacyjna funkcja poprawia doświadczenie użytkownika, umożliwiając obsługę bez użycia rąk, co jest szczególnie przydatne dla użytkowników w podróży lub tych, którzy preferują komendy głosowe.

Aby skorzystać z funkcji głosowego wyszukiwania:

1. Po prostu wypowiedz komendę po wejściu w tryb głosowego wyszukiwania.
2. PyAssist przetworzy twoją wypowiedź i wykonają odpowiednią akcję.

Ta funkcja dodaje nowy wymiar do interfejsu użytkownika, sprawiając, że PyAssist staje się jeszcze bardziej dostępny i przyjazny.

### Menu główne

Po uruchomieniu PyAssist zostaniesz powitany w menu głównym, gdzie możesz wybrać spośród następujących opcji:

- `addressbook:` Dostęp do menu zarządzania książką adresową.
- `notes:` Dostęp do menu zarządzania notatkami.
- `sort:` Sortowanie plików w określonym katalogu.
- `exit:` Wyjście z PyAssist.

### Menu książki adresowej

W menu książki adresowej możesz wykonywać następujące czynności:

- `add:` Dodaj nowy rekord do książki adresowej.
- `edit:` Edytuj istniejący rekord w książce adresowej.
- `show:` Wyświetl wszystkie rekordy lub określony rekord w książce adresowej.
- `delete:` Usuń rekord z książki adresowej.
- `export:` Wyeksportuj książkę adresową do pliku CSV.
- `import:` Importuj dane z pliku CSV do książki adresowej.
- `birthday:` Przeglądaj nadchodzące urodziny w określonym zakresie dni.
- `search:` Szukaj określonego rekordu w książce adresowej.

### Menu notatek

W menu notatek możesz zarządzać swoimi notatkami:

- `show:` Wyświetl wszystkie notatki.
- `search:` Szukaj określonej notatki.
- `create:` Stwórz nową notatkę.
- `edit:` Edytuj istniejącą notatkę.
- `delete:` Usuń notatkę.
- `addtag:` Dodaj tag do notatki.
- `findtag:` Znajdź notatki według określonego tagu.
- `sorttag:` Sortuj notatki według tagu.
- `export:` Eksportuj notatki do pliku.
- `import:` Importuj notatki z pliku.

### Sortowanie plików

PyAssist umożliwia sortowanie plików w określonym katalogu. Po prostu wybierz opcję "sort" z menu głównego i postępuj zgodnie z instrukcjami, aby podać ścieżkę do katalogu.

### Wyjście z Pyassist

Aby wyjść z PyAssist i zapisać dane, wybierz opcję "exit" z menu głównego.

### Struktura projektu

Projekt PyAssist jest zorganizowany w następujący sposób:

- `pyassist.py:` Główny skrypt inicjujący i uruchamiający aplikację PyAssist.
- `utility:` Katalog zawierający różne moduły narzędziowe używane przez PyAssist.
- `addressbook.py:` Definiuje klasę AddressBook do zarządzania rekordami książki adresowej.
- `record.py:` Definiuje klasę Record do przechowywania indywidualnych rekordów.
- `name.py:` Definiuje klasę Name do obsługi nazw.
- `phone.py:` Definiuje klasę Phone do obsługi numerów telefonu.
- `email.py:` Definiuje klasę Email do obsługi adresów e-mail.
- `birthday.py:` Definiuje klasę Birthday do obsługi dat urodzin.
- `notes.py:` Definiuje klasę Note do zarządzania notatkami.
- `sorter.py:` Definiuje klasę FileSorter do sortowania plików w katalogu.
- `notes_interaction.py:` Zawiera funkcje do interakcji z notatkami.
- `record_interaction.py:` Zawiera funkcje do interakcji z rekordami książki adresowej.
- `cmd_complet.py:` Definiuje klasę CommandCompleter do automatycznego uzupełniania poleceń wiersza poleceń.

## Konfiguracja

Upewnij się, że na Twoim komputerze zainstalowany jest Python 3.11.

Aplikacja korzysta z następujących bibliotek:

- 'SpeechRecognition'
- 'pyttsx3'
- 'pyaudio'
- 'pyfiglet'
- 'cowsay'
- 'difflib'
- 'prompt_toolkit'

## Instalacja

1. Pobierz repozytorium:

```
git clone https://github.com/Szumapman/PyAssist.git
```

2. Przejdź do katalogu z aplikacja:

```
cd PyAssist
```

3. Zainstaluj zależności:

Aby zainstalować pakiet z kodu źródłowego, wykonaj w konsoli polecenie `pip install .` lub `pip install -e .` w folderze, w którym znajduje się setup.py

## Uruchomienie programu

Uruchom aplikację za pomocą następującej komendy:

```
pyassist
```

## Funkcje

W kodzie PyAssist znajduje się kilka kluczowych funkcji umożliwiających interaktywne zarządzanie danymi w zorganizowany sposób. Oto krótki opis głównych funkcji zawartych w kodzie:

### 1. Dodawanie, Edytowanie i Usuwanie Kontaktów (Książka Adresowa)

#### Funkcja `add_record(record: Record)` w klasie `AddressBook`:

Dodaje nowy kontakt do książki adresowej. Sprawdza, czy dodany obiekt jest instancją klasy `Record`, co zapewnia poprawność danych kontaktowych.

#### Funkcja `edit_record(ADDRESSBOOK, *args)` w klasie `Record`:

Umożliwia edytowanie istniejącego kontaktu w książce adresowej, umożliwiając zmiany danych, takich jak numery telefonów, adresy e-mail itp.

#### Funkcja `del_record(ADDRESSBOOK, *args)` w klasie `Record`:

Usuwa kontakt z książki adresowej.

### 2. Wyświetlanie i Wyszukiwanie Kontaktów

#### Funkcja `show_names()` w klasie `AddressBook`:

Zwraca sformatowany ciąg zawierający wszystkie nazwy (klucze) w książce adresowej.

#### Funkcja `iterator(no_of_contacts_to_return=3)` w klasie `AddressBook`:

Iteruje przez rekordy i zwraca sformatowane informacje w grupach o określonym rozmiarze, ułatwiając przeglądanie kontaktów.

#### Funkcja `search(query: str)` w klasie `AddressBook`:

Wyszukuje kontakty w książce adresowej na podstawie podanego zapytania i zwraca nowy obiekt klasy `AddressBook`, dopasowany do zapytania.

### 3. Zarządzanie Notatkami

Funkcje w klasie `NotesMenuCommands` (plik `notes.py`): Pozwalają na wyświetlanie, tworzenie, edytowanie, usuwanie, dodawanie tagów, wyszukiwanie i sortowanie notatek.

### 4. Funkcja Sortowania Plików

#### Funkcja `sort_files_command(*args)` w głównym kodzie:

Sortuje pliki w określonym katalogu, co może być przydatne do organizowania danych na dysku.

### 5. Funkcjonalność Wyszukiwania Głosowego

Funkcje w głównym kodzie: Wprowadziły innowacyjną funkcję wyszukiwania głosowego, pozwalając użytkownikom na interakcję z narzędziem za pomocą poleceń głosowych. Włączając tryb wyszukiwania głosowego, użytkownicy mogą wydawać polecenia za pomocą mowy.

### 6. Funkcje Exportu i Importu

#### Funkcje `export_to_csv(filename: str)` i `import_from_csv(filename: str)` w klasie `AddressBook`

Pozwalają na eksportowanie i importowanie danych kontaktowych do i z plików CSV.

### 7. Obsługa Błędów

Dekorator `@error_handler` w głównym kodzie: Zapewnia obsługę błędów podczas dodawania, edytowania, eksportowania i innych operacji, poprawiając niezawodność programu.

Zintegrowane przykłady użycia w sekcji README umożliwiają szybkie zrozumienie, jak korzystać z poszczególnych funkcji PyAssist.

## Przykłady użycia

### Dodawanie Nowego Kontaktu do Książki Adresowej

![dodawanie_danych_do_ka](https://github.com/Szumapman/PyAssist/assets/115115006/ae247f21-363a-479b-a876-6df3c7d4eecf)
![dodawanie_danych_do_ka_2](https://github.com/Szumapman/PyAssist/assets/115115006/a9c5525c-a3f5-4dcc-9b90-d9170f3efe18)


### Korzystanie z Wyszukiwania Głosowego
![notatka_glosowa](https://github.com/Szumapman/PyAssist/assets/115115006/a2092da0-938b-40a8-b20d-443a961f9021)
![notatka_głosowa2](https://github.com/Szumapman/PyAssist/assets/115115006/4f600d96-4df7-4616-be66-33296f167c5e)
<!-- sc -->

## Licencja

Ta aplikacja jest udostępniana na licencji MIT.

## Autorzy

- 'Beata Chrząszcz'
- 'Jakub Szymaniak'
- 'Julia Macha'
- 'Paweł Szumański'
- 'Sabina Limmer'

## Kontakt

Jeśli masz pytania, sugestie lub chciałbyś się skontaktować w sprawie aplikacji, skontaktuj się z nami:

- GitHub Beata Chrząszcz: [BettyBeetle](https://github.com/BettyBeetle)
- GitHub Jakub Szymaniak: [jszymaniak](https://github.com/jszymaniak)
- GitHub Julia Macha: [juliazmacha](https://github.com/juliazmacha)
- GitHub Paweł Szumański: [Szumapman](https://github.com/Szumapman)
- GitHub Sabina Limmer: [SabinaLimmer](https://github.com/SabinaLimmer)

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

Make sure that Python 3.11 is installed on your computer.

The application uses the following libraries:

- 'SpeechRecognition'
- 'pyttsx3'
- 'pyaudio'
- 'pyfiglet'
- 'cowsay'
- 'difflib'
- 'prompt_toolkit'

## Installation

1. Download the repository:

```
git clone https://github.com/Szumapman/PyAssist.git
```

2. navigate to the directory with the application:

```
cd PyAssist
```

3. Install dependencies:

To install the package from the source code, type `pip install .` in the console or `pip install -e .` in the folder where setup.py is located

## Running the application

Run the application using the following command:

```
pyassist
```

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

![dodawanie_danych_do_ka](https://github.com/Szumapman/PyAssist/assets/115115006/ae247f21-363a-479b-a876-6df3c7d4eecf)
![dodawanie_danych_do_ka_2](https://github.com/Szumapman/PyAssist/assets/115115006/a9c5525c-a3f5-4dcc-9b90-d9170f3efe18)


### Using Voice Search

![notatka_glosowa](https://github.com/Szumapman/PyAssist/assets/115115006/a2092da0-938b-40a8-b20d-443a961f9021)
![notatka_głosowa2](https://github.com/Szumapman/PyAssist/assets/115115006/4f600d96-4df7-4616-be66-33296f167c5e)

## Licence

This application is made available under the MIT licence.

## Authors

- 'Beata Chrząszcz'
- 'Jakub Szymaniak'
- 'Julia Macha'
- 'Paweł Szumański'
- 'Sabina Limmer'

## Contact

If you have any questions, suggestions or would like to get in touch about the application, please contact us:

- GitHub Beata Chrząszcz: [BettyBeetle](https://github.com/BettyBeetle)
- GitHub Jakub Szymaniak: [jszymaniak](https://github.com/jszymaniak)
- GitHub Julia Macha: [juliazmacha](https://github.com/juliazmacha)
- GitHub Paweł Szumański: [Szumapman](https://github.com/Szumapman)
- GitHub Sabina Limmer: [SabinaLimmer](https://github.com/SabinaLimmer)
