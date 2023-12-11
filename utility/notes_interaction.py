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
def display_notes(notes, *args):
    notes_to_show = ""
    for i, note in enumerate(notes):
        notes_to_show += f"Note {i+1}:\n{note}\n{'-'*30}\n"
    return notes_to_show

# def create_note():
#     title = input("Enter note title: ")
#     choice = prompt("Do you want to type the note manually (type) or dictate it (dictate)? ", completer=CommandCompleter(["type", "dictate"])).lower() 
#     if choice == 'type':
#         content = input("Enter note content: ")
#         new_note = Note(title, content)
#         notes.append(new_note)
#         return f"Note created successfully."
#     elif choice == 'dictate':
#         content = getText()
#         if not content == 0:
#             print(f"{content}")
#             mow(content)
#             new_note = Note(title, content)           
#         else:
#             return"I couldn't recognize voice. Note created unsuccessfully."
#     else:
#         return "Invalid choice. Note creation failed."

#     new_note = Note(title, content)
#     notes.append(new_note)
#     return f"Note created successfully."

# def edit_note():
#     display_notes(notes)
#     choice = int(input("Enter the note number you want to edit: "))
#     if 1 <= choice <= len(notes):
#         new_content = input("Enter new content: ")
#         notes[choice - 1].edit_content(new_content)
#         return f"Note edited successfully."
#     else:
#         return f"Invalid note number."

# def delete_note():
#     display_notes(notes)
#     choice = int(input("Enter the note number you want to delete: "))
#     if 1 <= choice <= len(notes):
#         notes[choice - 1].remove_note(notes)
#         return f"Note deleted successfully."
#     else:
#         return f"Invalid note number."

# def add_tag_to_note():
#     display_notes(notes)
#     choice = int(input("Enter the note number you want to add a tag to: "))
#     if 1 <= choice <= len(notes):
#         tag = input("Enter tag to add: ")
#         notes[choice - 1].add_tag(tag)
#         return f"Tag '{tag}' added to the note."
#     else:
#         return f"Invalid note number."

# def find_notes_by_tag():
#     tag = input("Enter tag to search notes: ")
#     found_notes = Note.find_note_by_tag(notes, tag)
#     if found_notes:
#         display_notes(found_notes)
#         return f"Notes with tag '{tag}'"
#     else:
#         return f"No notes found with tag '{tag}'."
    
# def sort_notes_by_tag(*args):
#     Note.sort_notes_by_tag(notes)
#     return "Notes sorted by tags."



def find_note(notes, *args):
    if not args:
        search_term = input("Enter a keyword to search for in note: ")
    else:
        search_term = " ".join(args)
    found_notes = Note.find_notes(notes, search_term) 
    if found_notes:
        print(found_notes)
        return f"Notes containing '{search_term}:'\n{display_notes(found_notes)}"
    else:
        return f"No notes found containing '{search_term}'."
    

# def save_note(*args):
#     Note.save_notes(notes, NOTES_DATA_PATH)
#     return f"Notes exported."


# def load_note(*args):
#     global notes
#     notes = Note.load_notes(NOTES_DATA_PATH)
#     return f"Notes imported."