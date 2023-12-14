from pathlib import Path
from datetime import datetime
import csv

# notes = []
class Note:
    def __init__(self, title, content, tags=[]):
        self.title = title
        self.content = content
        self.create_time = datetime.now()
        self.modified_time = self.create_time
        self.tags = tags
    
    def __str__(self):
        creation_time_str = self.create_time.strftime("%Y-%m-%d %H:%M:%S")
        modified_time_str = self.modified_time.strftime("%Y-%m-%d %H:%M:%S")          
        tags_str = ", ".join(self.tags) if self.tags else "-----"     
        return (
            f"Title: {self.title}\n"
            f"Content: {self.content}\n"
            f"Creation Time: {creation_time_str}\n"
            f"Last Modified Time: {modified_time_str}\n"
            f"Tags: {tags_str}\n"
        )
    
    """
    Class Note allow you to create a note title, content, tag, creation time,
    editing time and deleting the entire note. It is also possible to save the content to a separate .csv file
    with the given name and reading notes from the .csv file. 
    """


    def edit_content(self, new_content):     #edit content of note and update modified time
        self.content = new_content
        self.modified_time = datetime.now()

    def find_notes(notes_list, keyword):     #search note with input keyword
        keyword = keyword.lower()
        found_notes = []
        for note in notes_list:
            if keyword in note.title.lower() or keyword in note.content.lower():
                found_notes.append(note)
        return found_notes
                

    @staticmethod
    def sort_notes_by_tag(notes_list):      #mechanism that sorts notes by tag (added to add, change, remove tag)
        notes_list.sort(key=lambda note: ", ".join(note.tags))

    def add_tag(self, tag):     #add tag to the note if it doesnt exist and update modified time
        if tag not in self.tags:
            self.tags.append(tag)
            self.modified_time = datetime.now()
            Note.sort_notes_by_tag(notes)

    def change_tag(self, old_tag, new_tag):     #changing tag and update modified time
        if old_tag in self.tags:
            index = self.tags.index(old_tag)
            self.tags[index] = new_tag
            self.modified_time = datetime.now()
            Note.sort_notes_by_tag(notes)

    def remove_tag(self, tag):      #remove tag from note
        if tag in self.tags:
            self.tags.remove(tag)
            self.modified_time = datetime.now()
            Note.sort_notes_by_tag(notes)

    def find_note_by_tag(notes_list, tag):  #returns list of notes with specified tag
        note_tag = []
        for note in notes_list:
            if tag in note.tags:
                note_tag.append(note)
        return note_tag
    
        
    def remove_note(self, notes_list):
        notes_list.remove(self)

    def save_notes(notes_list, file_name):   #saving notes to .csv file        
        """
        Save a collection of Note objects to a CSV file.

        Parameters:
        - notes_list (list): A list containing Note objects to be saved.
        - file_name (str): The name of the CSV file to which notes will be saved.

        This method writes the attributes of each Note object (title, content, creation time,
        modified time, and tags) to the specified CSV file. If the file does not exist,
        it will be created. If it already exists, it will be overwritten.
        """
        try:
            with open(file_name, mode="w", newline="", encoding="utf-8") as file:  
                writer = csv.writer(file)
                writer.writerow(["Title", "Content", "Creation Time", "Last Modified Time", "Tags"])  #header

                for note in notes_list:
                    writer.writerow([note.title, note.content, note.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                                    note.modified_time.strftime("%Y-%m-%d %H:%M:%S"), ", ".join(note.tags)])
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error saving notes to {file_name}: {e}")

    def load_notes(file_name):      #loading .csv file with notes
        """
        Load Note objects from a CSV file.

        Parameters:
        - file_name (str): The name of the CSV file from which notes will be loaded.

        This method reads Note objects (title, content, creation time, modified time, and tags)
        from the specified CSV file. It parses each row in the file to create Note objects and
        returns them as a list. If the file is empty, missing headers, or encounters errors while
        loading, it returns an empty list.
        """
        try:
            if Path.exists(file_name):
                loaded_notes = []
                with open(file_name, mode="r", encoding="utf-8") as file:
                    reader = csv.reader(file)
                    header = next(reader, None)
                    if header is None:
                        print("Empty file or missing header.")
                        return []
                    
                    for row in reader:
                        if row:
                            title, content, creation_time_str, modified_time_str, tags_str = row
                            create_time = datetime.strptime(creation_time_str, "%Y-%m-%d %H:%M:%S")
                            modified_time = datetime.strptime(modified_time_str, "%Y-%m-%d %H:%M:%S")
                            tags = tags_str.split(', ') if tags_str else []
                            new_note = Note(title, content)
                            new_note.create_time = create_time
                            new_note.modified_time = modified_time
                            new_note.tags = tags
                            loaded_notes.append(new_note)
                return loaded_notes
            return []
        except (FileNotFoundError, PermissionError, ValueError, csv.Error) as e:
            print(f"Error loading notes from {file_name}: {e}")
            return []
