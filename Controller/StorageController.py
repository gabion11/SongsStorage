import shutil
import os


class StorageController:
    """
    A class to represent the Storage Controller

    ...
    Attributes
    ----------
    destination: Path

    Methods
    -------
    insert_song(source)
    Insets a song in destination folder.

    delete_song(file_path)
    Deletes a song from destination.
    """
    def __init__(self, _destination):
        self.destination = _destination

    def insert_song(self, source):
        """
            Insets a song in destination folder.

        :param source: a path file
        :return:  the path to the newly created file
        """
        return shutil.copy(source, self.destination)

    @staticmethod
    def delete_song(file_path):
        """
         Deletes a song from destination.
        :param file_path: Path of the file to be deleted
        """
        os.remove(file_path)
