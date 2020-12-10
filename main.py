from datetime import date

from Controller.MetadataController import MetadataController

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    meta = MetadataController()
    # meta.delete_metadata(1)
    # meta.insert_metadata("Storage", "FS", "Summner", date(1970, 10, 8), "#hello")
    songs = meta.update_file_name(2, {"FileName": "storage", "Artist": "Vl"})
    meta.print_metadata(songs)
    songs = meta.get_metadata()
    for song in songs:
        meta.print_metadata(song)

