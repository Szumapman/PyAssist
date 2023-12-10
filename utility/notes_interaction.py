from utility.notes import Note
import os

# paths to files with data
NOTES_DATA_PATH = os.path.join(os.getcwd(), "notes.csv")

#objects storing data while the program is running
NOTES = Note.load_notes(NOTES_DATA_PATH)
notes = NOTES if NOTES else []
#functions for note command
def display_notes(notes_list):
    if not notes_list:
        return f"No notes available."
    else:
        for i, note in enumerate(notes_list):
            print(f"Note {i+1}:")
            print(note)
            print("-" * 30)

def create_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
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
    return f"Saved."
def load_note(*args):
    global notes
    notes = Note.load_notes(NOTES_DATA_PATH)
    return f"Load complete."