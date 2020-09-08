import shutil
import uuid


class FileCopier:

    def __init__(self, path_to_files, file):
        self.path_to_files = path_to_files
        self.file = file

    def get_filename_without_extension(self):
        if not self.file:
            return
        if '.' in self.file:
            return self.file.rsplit('.', 1)[0].lower()
        else:
            return None

    def copy_file(self):
        filename = self.get_filename_without_extension()
        if not filename:
            return None
        path_to_new_file = f"{self.path_to_files}/" + filename + "-copy-id-" + str(uuid.uuid4()) + ".txt"
        path_to_f = f"{self.path_to_files}/" + self.file
        print(f"The file {path_to_new_file} has been created")
        shutil.copyfile(path_to_f, path_to_new_file)
        return path_to_new_file
