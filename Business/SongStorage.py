import zipfile
import webbrowser
from datetime import datetime
from pathlib import Path
from Controller.MetadataController import MetadataController
from Controller.StorageController import StorageController
from Proprieties import proprieties


class SongStorage:
    """
    A class to represent the business of application

    Attributes
    ----------
    metaController: an instance of the class MetadataController
    storageController: an instance of the class StorageController

    Methods
    -------
    add_song()
        Add a song into storage and metadata in database
    delete_song()
        Delete a song from storage and metadata from database
    modify_data()
        Modifies a song by it's id
    search()
        Search songs in the database
    create_save_list()
        Create a zip with a list of songs
    play()
        Play a song
    display_all()
        Display all the song from database
    run()
        Execute commands

    """
    def __init__(self):
        self.metaController = MetadataController()
        self.storageController = StorageController(proprieties.storage_destination)

    def add_song(self):
        """
        Reads from keyboard a file path, artist name, release date, tags and add the file in storage and the
        metadata in database
        It will print the id of song if it was successful added
        else a error message
        """
        _id = None
        file_path = input("path: ")
        artist = input("artist:")
        release_date = input("release_date:")
        tags = input("tags")

        song_name = Path(file_path)
        if song_name.exists():

            file_path = self.storageController.insert_song(file_path)
            _id = self.metaController. \
                insert_metadata(file_path, artist, song_name.name,
                                datetime.strptime(release_date, '%d %m %Y'), tags)

            if _id is None:
                print("fail adding the song")
            else:
                print("the song was added with id= ", _id)
        else:
            print("Wrong path")

    def delete_song(self):
        """
        Reads an id and deletes the song from storage folder and the metadata from database

        """
        _id = input("id:")
        song = self.metaController.get_by_id(_id)
        if song is None:
            print("This id did not exist")
        else:
            file_path = song.FileName
            self.metaController.delete_metadata(_id)
            self.storageController.delete_song(file_path)
            print("Delete successful")

    def modify_data(self):
        """
        Modifies a song by it's id
        Reads metadata from keyboard, if a metadata is skipped the old value will remain the same

        """
        _id = input("Id: ")
        if self.metaController.get_by_id(_id) is not None:
            artist = input("artist:")
            song_name = input("song name:")
            release_date = input("release_date:")
            tags = input("tags")
            new_data = dict()
            if song_name is not "":
                new_data["SongName"] = song_name
            if artist is not "":
                new_data["Artist"] = artist
            if release_date is not "":
                new_data["ReleaseDate"] = datetime.strptime(release_date, '%d %m %Y')
            if tags is not "":
                new_data["Tags"] = tags
            self.metaController.update_metadata(_id, new_data)

        else:
            print("This id did not exist")

    def search(self):
        """
        Searches a song by metadata read from keyboard
        Prints a list with all the songs found
        """
        artist = input("Artist")
        song_name = input("song name:")
        tags = input("tags")

        new_data = dict()
        if song_name is not "":
            new_data["SongName"] = song_name
        if artist is not "":
            new_data["Artist"] = artist
        if tags is not "":
            new_data["Tags"] = tags
        songs = self.metaController.get_metadata(new_data)
        if songs.count() == 0:
            print("No songs founded")
        for song in songs:
            self.metaController.print_metadata(song)

    def create_save_list(self):
        """
        Creates an zip archive with the songs with the specific metadata

        """
        path = input("output path: ")
        artist = input("Artist")
        song_name = input("song name:")
        tags = input("tags")

        new_data = dict()
        if song_name is not "":
            new_data["SongName"] = song_name
        if artist is not "":
            new_data["Artist"] = artist
        if tags is not "":
            new_data["Tags"] = tags
        songs = self.metaController.get_metadata(new_data)

        if songs.count() == 0:
            print("No songs founded")
        else:
            try:
                _zip = zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED)
                for song in songs:
                    _zip.write(song.FileName)
                _zip.close()
            except FileNotFoundError:
                print("Wrong Path")


    def play_song(self):
        """
        Reads an id from keyboard and play a the song using web browser library

        """
        _id = input("id:")
        song = self.metaController.get_by_id(_id)
        if song is not None:
            webbrowser.open(song.FileName)
        else:
            print("This id did not exist")

    def display_all(self):
        """
        Display all songs from database
        """
        songs = self.metaController.get_all_metadata()
        for song in songs:
            self.metaController.print_metadata(song)

    def run(self):
        """
        Reads commands from keyboard and execute them
        If a command didn't exist will display an error message

        """
        command = input("Introduceti o comanda")

        while command != "quit":

            if command == "Add_song":
                self.add_song()
            elif command == "Delete_song":
                self.delete_song()
            elif command == "Modify_data":
                self.modify_data()
            elif command == "Search":
                self.search()
            elif command == "Create_save_list":
                self.create_save_list()
            elif command == "Play":
                self.play_song()
            elif command == "Display_all":
                self.display_all()
            else:
                print("wrong command")

            command = input("Introduceti o comanda")

        print("bye")
