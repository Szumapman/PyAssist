from datetime import datetime

notes = []
class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.create_time = datetime.now()
        self.modified_time = self.create_time
        self.tags = []
    
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

    def edit_content__(self, new_content):     #edit content of note and update modified time
        self.content = new_content
        self.modified_time = datetime.now()

    def add_tag(self, tag):     #add tag to the note if it doesnt exist and update modified time
        if tag not in self.tags:
            self.tags.append(tag)
            self.modified_time = datetime.now()

    def change_tag(self, old_tag, new_tag):     #changing tag and update modified time
        if old_tag in self.tags:
            index = self.tags.index(old_tag)
            self.tags[index] = new_tag
            self.modified_time = datetime.now()

    def remove_tag(self, tag):      #remove tag from note
        if tag in self.tags:
            self.tags.remove(tag)
            self.modified_time = datetime.now()

    def find_note_by_tag(notes_list, tag):  #returns list of notes with specified tag
        note_tag = []
        for note in notes_list:
            if tag in note.tags:
                note_tag.append(note)
        return note_tag

            
    def remove_note(self, notes_list):
        notes_list.remove(self)

'''debug code below'''

# note1 = Note("Meeting Agenda", "something something.")
# note1.add_tag("meeting")
# note1.add_tag("project")

# note2 = Note("Shopping List", "another something.")
# note2.add_tag("shopping")

# note3 = Note("Ideas", "yet another some.....")
# note3.add_tag("project")

# notes = [note1, note2, note3]


# found_notes = Note.find_note_by_tag(notes, "project")
# for note in found_notes:
#     print(note)
