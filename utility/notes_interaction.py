from utility.notes import Note
from utility.recognizer import mow, getText
from utility.cmd_complet import CommandCompleter

from prompt_toolkit import prompt
import os
"""
This script provides a set of functions to manage notes, allowing users to create, 
edit, delete, and search notes based on titles, contents, and tags. It utilizes a 'Note' 
class to handle note-related operations, enabling the creation of notes either manually or 
via dictation, editing existing notes, adding tags, searching by tags, and exporting/importing 
notes to/from a .csv file.
"""
# paths to files with data
current_dir = os.path.dirname(os.path.abspath(__file__))
NOTES_DATA_PATH = os.path.join(current_dir, "data/notes.csv")

#objects storing data while the program is running
NOTES = Note.load_notes(NOTES_DATA_PATH)
notes = NOTES if NOTES else []

#functions for note command
def display_notes(notes_list):
    if not notes_list:
        print("No notes available.")
    else:
        for i, note in enumerate(notes_list):
            print(f"Note {i+1}:")
            print(note)
            print("-" * 30)

def create_note():
    title = input("Enter note title: ")
    choice = prompt("Do you want to type the note manually (type) or dictate it (dictate)? ", completer=CommandCompleter(["type", "dictate"])).lower() 
    if choice == 'type':
        content = input("Enter note content: ")
        new_note = Note(title, content)
        notes.append(new_note)
        return f"Note created successfully."
    elif choice == 'dictate':
        content = getText()
        if not content == 0:
            print(f"{content}")
            mow(content)
            new_note = Note(title, content)           
        else:
            return"I couldn't recognize voice. Note created unsuccessfully."
    else:
        return "Invalid choice. Note creation failed."

    new_note = Note(title, content)
    notes.append(new_note)
    return f"Note created successfully."

def edit_note():
    display_notes(notes)
    choice = int(input("Enter the note number you want to edit: "))
    if 1 <= choice <= len(notes):
        new_content = input("Enter new content: ")
        notes[choice - 1].edit_content(new_content)
        return f"Note edited successfully."
    else:
        return f"Invalid note number."

def delete_note():
    display_notes(notes)
    choice = int(input("Enter the note number you want to delete: "))
    if 1 <= choice <= len(notes):
        notes[choice - 1].remove_note(notes)
        return f"Note deleted successfully."
    else:
        return f"Invalid note number."

def add_tag_to_note():
    display_notes(notes)
    choice = int(input("Enter the note number you want to add a tag to: "))
    if 1 <= choice <= len(notes):
        tag = input("Enter tag to add: ")
        notes[choice - 1].add_tag(tag)
        return f"Tag '{tag}' added to the note."
    else:
        return f"Invalid note number."

def find_notes_by_tag():
    tag = input("Enter tag to search notes: ")
    found_notes = Note.find_note_by_tag(notes, tag)
    if found_notes:
        display_notes(found_notes)
        return f"Notes with tag '{tag}'"
    else:
        return f"No notes found with tag '{tag}'."
    
def sort_notes_by_tag(*args):
    Note.sort_notes_by_tag(notes)
    return "Notes sorted by tags."



def find_note():
    search_term = input("Enter a keyword to search for in note titles or contents: ")
    found_notes = Note.find_notes(notes, search_term)
    if found_notes:
        display_notes(found_notes)
        return f"Notes containing '{search_term}'"
    else:
        return f"No notes found containing '{search_term}'."
    

def save_note(*args):
    Note.save_notes(notes, NOTES_DATA_PATH)
    return f"Notes exported."
def load_note(*args):
    global notes
    notes = Note.load_notes(NOTES_DATA_PATH)
    return f"Notes imported."