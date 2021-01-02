import shutil
import os
import glob
from pathlib import Path


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

    compareFiles(file1, file2):
    Compares binary two files
    """

    def __init__(self, _destination):
        self.destination = _destination
        self.counter = 1

    def insert_song(self, source):
        """
            Insets a song in destination folder. If the song name already exists, compare files binary if the content is
            different rename the current file

        :param source: a path file
        :return:  the path to the newly created file
        """

        song_name = Path(source)
        files = glob.glob(self.destination+'/*')

        for file in files:
            file = Path(file)
            if file.name == song_name.name:
                # verify if the content is the same
                if not self.compareFiles(file, source):
                    name_without_ext = song_name.stem
                    ext = song_name.suffix
                    try:
                        song_name.rename(Path(song_name.parent, f"{name_without_ext}_{self.counter}_{ext}"))

                    except PermissionError:
                        print("Permission denied")
                    except IOError:
                        print("try again")

                    source = str(source).replace(f"{name_without_ext}{ext}", f"{name_without_ext}_{self.counter}_{ext}")
                    self.counter += 1
        try:
            return shutil.copy(source, self.destination)
        except IOError:
            print("Error copping the file")

    @staticmethod
    def delete_song(file_path):
        """
         Deletes a song from destination.
        :param file_path: Path of the file to be deleted
        """
        try:
            os.remove(file_path)
        except IOError:
            print("Error removing the file")

    @staticmethod
    def compareFiles(file1, file2):
        """
        Compares binary two files
        :param file1: File Path of file number one
        :param file2: File Path of file number two
        :return: true if file1 is equal with file2
                false otherwise
        """
        try:
            with open(file1, "rb") as one:
                with open(file2, "rb") as two:
                    chunk = other = True
                    while chunk or other:
                        chunk = one.read(1000)
                        other = two.read(1000)
                        if chunk != other:
                            return False
                    return True
        except IOError:
            print("Unable to open the files")
