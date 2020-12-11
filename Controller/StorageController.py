import shutil
import os


class StorageController:

    def __init__(self, dest):
        self.destination = dest

    def insert_song(self, source):
        shutil.copy(source, self.destination)

    @staticmethod
    def delete_song(file_path):
        os.remove(file_path)
