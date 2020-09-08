import os
from text_formatter import TextFormatter
from file_copier import FileCopier
import hashlib

import enum


class FromOptions(enum.Enum):
    TABS = 'tabs'
    SPACES = 'spaces'


class TextFileManager:
    path = "text_files"
    modifiedLine = 0

    def __init__(self, _from, _replace, _tab_chars):
        self.from_ = _from
        self.replace = _replace
        self.chars = _tab_chars

        self.convert_text()

    @staticmethod
    def hashfile(path, blocksize=65536):
        afile = open(path, 'rb')
        hasher = hashlib.md5()
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)
        afile.close()
        return hasher.hexdigest()

    def find_dup(self, parent_folder):
        # Dups in format {hash:[names]}
        dups = {}
        for dirName, subdirs, fileList in os.walk(parent_folder):
            print('Scanning %s...' % dirName)
            for filename in fileList:
                # Get the path to the file
                path = os.path.join(dirName, filename)
                # Calculate hash
                file_hash = self.hashfile(path)
                # Add or append the file path
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups

    @staticmethod
    def print_space(number_of_space):
        arr = []
        x = "-"
        for i in range(number_of_space):
            arr.append(x)
        res = ''.join(arr)
        print(res)
        return res

    def get_file_to_format(self):
        file_hash = self.find_dup(self.path)
        files_to_format = []
        for f in file_hash:
            # d.append(file_hash[f])
            x = list(sorted(file_hash[f], key=len))
            if len(x) > 0:
                # print(x[0])
                # print(self.path)
                y = x[0].split(self.path + '/')[1]
                files_to_format.append(y)
        return files_to_format

    def convert_text(self):

        files_to_format = self.get_file_to_format()
        print("Number of files to edit: " + str(len(files_to_format)))
        print("List of files to edit: " + str(files_to_format))
        self.print_space(50)
        for file in files_to_format:
            if not self.from_:
                text_formatter = TextFormatter(self.path, file, 4)
            else:
                if not self.chars:
                    self.chars = 4
                text_formatter = TextFormatter(self.path, file, self.chars)
            print("I am editing the file: " + str(file))
            if self.from_:
                if not self.replace:
                    file_copier = FileCopier(self.path, file)
                    file_copier.copy_file()

            if self.from_ == FromOptions.SPACES.value:
                text_formatter.space_to_tab()
            elif self.from_ == FromOptions.TABS.value:
                text_formatter.tab_to_space()
            else:
                res = text_formatter.analyze_file()
                text_formatter.print_analyze_file(res[0], res[1])
