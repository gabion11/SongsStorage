import glob
import shutil
import os
from pathlib import Path
import hashlib
from Controller.MetadataController import MetadataController


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
            Insets a song in destination folder.
            If create the folder if it didn't exist
            Save the file with his hash as file name

            different rename the current file

        :param source: a path file
        :return:  the path to the newly created file or None if an error appears
        """
        # check if the storage exist otherwise create this
        if Path(self.destination).exists():
            print("")
        else:
            print("Storage folder doesn't exist")

            try:
                os.mkdir(Path(self.destination))
            except:
                print("Error creating the folder")
                return None
            print("Storage created successfully")

        song_name = Path(source)
        hash_name = self.getHash(source)
        if hash_name == "":
            print("Error hashing the file")
            return None

        files = glob.glob(self.destination + '/*')
        # check if the file already exist
        for file in files:
            file = Path(file)
            if file.name == hash_name + song_name.suffix:
                return str(file).replace(chr(92), "/")

        # copy the file in the storage
        try:
            newPath = shutil.copy(source, self.destination)
        except:
            print("Error copying the file")
            return None

        song_name = Path(newPath)
        # rename the file with hash
        try:
            song_name.rename(Path(song_name.parent, f"{hash_name}{song_name.suffix}"))
        except:
            print("Error renaming the file")
            return None

        return str('Storage/' + hash_name+song_name.suffix)

    @staticmethod
    def delete_song(file_path):
        """
         Deletes a song from destination.
        :param file_path: Path of the file to be deleted
        :return True if the file was removed successfully
        """

        try:
            os.remove(file_path)
            return True
        except IOError:
            print("Error removing the file")

    @staticmethod
    def getHash(file_path):
        try:
            m = hashlib.sha1()
            f = open(file_path, "rb")
            while True:
                data = f.read(4096)
                if len(data) == 0:
                    break
                m.update(data)
            f.close()
            return m.hexdigest()
        except:
            return ""
