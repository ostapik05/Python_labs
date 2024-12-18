from shared.classes.KeyDataAccess import KeyDataAccess
from shared.services.FileOperations import *
from pathlib import Path


class FolderDataAccess(KeyDataAccess):
    def __init__(
        self, folder_path="assets/", is_without_extension=False, extensions=".txt"
    ):
        self.folder_path = Path(folder_path)
        self.is_without_extension = is_without_extension
        self.extensions = extensions

    def set(self, key, data):
        write_to_file(data, self.full_path(key))

    def get(self, key):
        return load_from_file(self.full_path(key))

    def full_path(self, file_name):
        if self.is_without_extension:
            file_name += self.extensions
        return Path(self.folder_path, file_name)
