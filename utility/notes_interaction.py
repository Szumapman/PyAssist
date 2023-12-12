from utility.notes import Note
from utility.recognizer import mow, getText
from utility.cmd_complet import CommandCompleter

from prompt_toolkit import prompt
import os

# paths to files with data
# NOTES_DATA_PATH = os.path.join(os.getcwd(), "data/notes.csv") # do usunięcia

#objects storing data while the program is running
# NOTES = Note.load_notes(NOTES_DATA_PATH)
# notes = [] # NOTES if NOTES else []

#functions for note command
def show_notes(notes, *args):
    return display_notes(notes, "Your notes:\n")

def display_notes(notes, notes_to_show):
    if not notes:
        return "Nothing to show."
    for i, note in enumerate(notes):
        notes_to_show += f"Note {i+1}:\n{note}\n{'-'*30}\n"
    return notes_to_show

def create_note(notes, *args):
    if not args:
        title = input("Enter note title: ")
        if title == "":
            return "Operation canceled."
    else:
        title = " ".join(args)
    while True:
        choice = prompt("Do you want to type the note manually (type) or dictate it (dictate)? ", completer=CommandCompleter(["type", "dictate"])).lower() 
        if choice == 'type':
            content = input("Enter note content: ")
            break
        elif choice == 'dictate':
            content = getText()
            if content != 0:
                print(f"{content}")
                mow(content)
                break         
            else:
                return"I couldn't recognize voice. Operation canceled."    
    tags = input("Tags (separated by space): ")
    tags = list(tags.split())
    new_note = Note(title, content, tags)
    notes.append(new_note)
    return f"Note created successfully."


def choice_note(notes, *args):
    if not args:
        print(display_notes(notes, "Your notes:\n"))
    else:
        query = " ".join(args)
        notes = find_note(notes, query)
        if notes:
            print(display_notes(notes, f"Your notes with {query}\n"))
        else:
            return f"You don't have notes with {query}"
    choice = int(input("Enter the number of the note you want to choose: "))
    return notes, choice   


def edit_note(notes, *args):
    notes, choice = choice_note(notes, *args)
    if 1 <= choice <= len(notes):
        new_content = input("Enter new content: ")
        notes[choice - 1].edit_content(new_content)
        return f"Note edited successfully."
    else:
        return f"Invalid note number."

def delete_note(notes, *args):
    notes, choice = choice_note(notes, *args)
    if 1 <= choice <= len(notes):
        notes[choice - 1].remove_note(notes)
        return f"Note deleted successfully."
    else:
        return f"Invalid note number."

def add_tag_to_note(notes, *args):
    notes, choice = choice_note(notes, *args)
    if 1 <= choice <= len(notes):
        tag = input("Enter tag to add: ")
        notes[choice - 1].add_tag(tag)
        return f"Tag '{tag}' added to the note."
    else:
        return f"Invalid note number."

def find_notes_by_tag(notes, *args):
    if not args:
        tag = input("Enter tag to search notes: ")
        found_notes = Note.find_note_by_tag(notes, tag)
    else:
        found_notes = []
        tag = " ".join(args)
        for arg in args:
            found_notes += Note.find_note_by_tag(notes, arg)
    if found_notes:
        return display_notes(found_notes, f"Notes with tag '{tag}'\n")
    else:
        return f"No notes found with tag '{tag}'."


#funkcja do poprawy / sprawdzenia    
def sort_notes_by_tag(notes, *args): 
    Note.sort_notes_by_tag(notes) #to sortowanie nie działe, albo ja nie rozumiem, co ono ma robić
    return display_notes(notes, "Notes sorted by tags.\n")


def show_search(notes, *args):
    if not args:
        search_term = input("Enter a keyword to search for in note: ")
    else:
        search_term = " ".join(args)    
    return display_notes(find_note(notes, search_term), f"Notes containing '{search_term}':\n")


def find_note(notes, query):
    return Note.find_notes(notes, query) 
    

# def save_note(*args):
#     Note.save_notes(notes, NOTES_DATA_PATH)
#     return f"Notes exported."


# def load_note(*args):
#     global notes
#     notes = Note.load_notes(NOTES_DATA_PATH)
#     return f"Notes imported."