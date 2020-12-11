import zipfile
import webbrowser
from datetime import datetime
from pathlib import Path
from Controller.MetadataController import MetadataController
from Controller.StorageController import StorageController


class SongStorage:

    def __init__(self):
        self.metaController = MetadataController()
        self.storageController = StorageController("D:/Anul III/Phyton/A9/Storage")

    def add_song(self):
        _id = None

        file_path = input("path: ")
        artist = input("artist:")
        release_date = input("release_date:")
        tags = input("tags")

        song_name = Path(file_path)
        if song_name.exists():

            self.storageController.insert_song(file_path)
            file_path = str(self.storageController.destination + '/' + song_name.name)
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
        _id = input("id:")
        song = self.metaController.get_by_id(_id)
        file_path = song.FileName
        self.metaController.delete_metadata(_id)
        self.storageController.delete_song(file_path)

    def modify_data(self):
        _id = input("Id: ")

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

    def search(self):

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
        for song in songs:
            self.metaController.print_metadata(song)

    def create_save_list(self):
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
        _zip = zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED)

        for song in songs:
            _zip.write(song.FileName)
        _zip.close()

    def play_song(self):
        _id = input("id:")
        song = self.metaController.get_by_id(_id)
        webbrowser.open(song.FileName)

    def display_all(self):
        songs = self.metaController.get_all_metadata()
        for song in songs:
            self.metaController.print_metadata(song)

    def run(self):

        command = input("Introduceti o comanda")

        while command != "quit":

            if command == "Add_song" or command == "1":
                self.add_song()

            elif command == "Delete_song" or command == "2":
                self.delete_song()
            elif command == "Modify_data" or command == "3":
                self.modify_data()
            elif command == "Search" or command == "4":
                self.search()
            elif command == "Create_sava_list" or command == "5":
                self.create_save_list()
            elif command == "Play" or command == "6":
                self.play_song()
            elif command == "Display_all" or command == "7":
                self.display_all()
            else:
                print("wrong command")
            command = input("Introduceti o comanda")

        print("bye")


