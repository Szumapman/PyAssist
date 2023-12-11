import os
import shutil
import unicodedata

class FileSorter:
    def __init__(self):
        self.folders = {
            'images': ('.jpeg', '.png', '.jpg', '.svg', '.gif', '.tiff', 'tif', '.bmp', '.raw'),
            'videos': ('.avi', '.mp4', '.mov', '.mkv', '.wmv', '.flv', '.webm'),
            'documents': ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx', '.rtf', '.key', '.ppt', '.xls', '.csv', '.ods'),
            'music': ('.mp3', '.ogg', '.wav', '.amr', '.aac', '.flac', '.wma', '.m4a'),
            'archives': ('.zip', '.gz', '.tar')
        }
    """This code organizes files within a folder and its subfolders based on their file extensions,
    making it easier to manage and navigate through data. Its key function involves automatically
    moving files to respective category folders according to their extensions. 
    Additionally, if a file is an archive, it gets unpacked and placed in a dedicated subfolder.
    This process covers all files in the main folder and its subdirectories, aiding in 
    comprehensive sorting and organization of files. This approach allows users to swiftly
    locate and manage various file types, thereby improving the overall structure and
    accessibility of stored data."""

    # method for normalizing and changing the file name
    def normalize_and_rename(self, text):
        def normalize(x):
            normalized = unicodedata.normalize("NFD", x)
            return ''.join([c for c in normalized if not unicodedata.combining(c)])

        old_name = text
        new_name = normalize(old_name)
        return new_name

    # method for sorting files in a given folder
    def sorter(self, folder):
        print(f"Sorting files in the given path: {folder}")

        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1].lower()

                if file_extension.endswith((".zip", ".tar", ".gz")):
                    # Unpacking files into appropriate subfolders within the 'archives' folder
                    zip_folder = os.path.splitext(filename)[0]
                    to_zip_folder = os.path.join(folder, "archives", zip_folder)
                    if not os.path.exists(to_zip_folder):
                        os.makedirs(to_zip_folder)
                    shutil.unpack_archive(file_path, to_zip_folder)
                    os.remove(file_path)
                else:
                    found_extensions = False
                    for category, extensions in self.folders.items():
                        if file_extension in extensions:
                            # Moving files to their respective folders
                            target_folder = os.path.join(folder, category)
                            if not os.path.exists(target_folder):
                                os.makedirs(target_folder)
                            shutil.move(file_path, os.path.join(target_folder, self.normalize_and_rename(filename)))
                            print(f"File {filename} moved to {category} folder.")
                            found_extensions = True
                            break
                    if not found_extensions:
                        print(f"Unknown extension found: <{file_extension}>")

    # method for processing a folder.
    def process_folder(self, folder):
        self.sorter(folder)
        for dirpath, dirnames, filenames in os.walk(folder):
            for dirname in dirnames:
                subfolder_path = os.path.join(dirpath, dirname)
                folder_name = os.path.basename(subfolder_path).lower()
                if folder_name in self.folders.keys():
                    continue
                self.sorter(subfolder_path)

            for dirname in dirnames:
                folder_to_check = os.path.join(dirpath, dirname)
                if not os.listdir(folder_to_check):
                    os.rmdir(folder_to_check)
                    print(f"Empty directory: <{dirname}> removed.")