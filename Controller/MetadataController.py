from Data.metadata import Metadate
from Data.base import Session, engine, Base

Base.metadata.create_all(engine)


class MetadataController:
    """
     A class to represent the Metadata  Controller

     ...
    Attributes
    ----------
    session: an instance of class Session
    Methods
    -------
    insert_metadata()
        Inserts a metadata in database
    get_all_metadata()
    delete_metadata()
        Delete a song from database
    get_metadata()
        Select songs from database
    get_by_id()
        Select a song by it's id from database
    update_metadata()
        Update a song by its id
    print_metadata()
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the MetadataController object
        """
        self.session = Session()

    def insert_metadata(self, filename, artist, song_name, release_date, tags):
        """
        Inserts a metadata in database

        :param filename: Path of the songs where is stored
        :param artist: Name of Artist
        :param song_name: Name of Song
        :param release_date: Release date of the song
        :param tags: List of tags
        :return: Id of the new inserted song
        """
        song1 = Metadate(filename, artist, song_name, release_date, tags)
        self.session.add(song1)
        self.session.commit()
        return song1.Id

    def get_all_metadata(self):
        """

        :return:Returns all data from database
        """
        songs = self.session.query(Metadate).all()
        return songs

    def delete_metadata(self, _id):
        """
        Delete a song from database by its id
        :param _id: id of the song

        """
        self.session.query(Metadate).filter_by(Id=_id).delete()
        self.session.commit()

    def get_metadata(self, metadata):
        """
        Select from database the songs that satisfy the metadata parameter
        :param metadata: a dictionary with the constrains for select
        :return: All songs founded
        """
        q = self.session.query(Metadate)
        for attr, value in metadata.items():
            q = q.filter(getattr(Metadate, attr).like("%%%s%%" % value))

        return q

    def get_by_id(self, _id):
        """
        Select a song by it's id from database
        :param _id: id of the song
        :return:the song from database else None
        """
        song = self.session.query(Metadate).get(_id)
        return song

    def update_metadata(self, _id, metadate):
        """
        Update a song by its id
        :param _id: id of the song
        :param metadate: a dictionary will all new metadata
        :return:Returns the updated song
        """
        self.session.query(Metadate).filter(Metadate.Id == _id).update(metadate, synchronize_session=False)
        self.session.commit()
        return self.get_by_id(_id)

    @staticmethod
    def print_metadata(meta):
        """
        Print a song to console
        :param meta: metadata to be displayed
        """
        print(f'{meta.Id}    {meta.Artist}    {meta.SongName}    {meta.ReleaseDate}    {meta.Tags} ')
