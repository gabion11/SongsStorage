from sqlalchemy import Column, String, Integer, Date

from Data.base import Base


class Metadate(Base):
    """
     A class to represent a metadata.

     ...
     Attributes
     ----------
     filename: Path of the locations
     artist: Artist name
     song_name: Song Name
     release_date: Release date
     tags:List of tags
    """
    __tablename__ = 'metadata'

    Id = Column(Integer, primary_key=True)
    FileName = Column(String)
    Artist = Column(String)
    SongName = Column(String)
    ReleaseDate = Column(Date)
    Tags = Column(String)

    def __init__(self, filename, artist, song_name, release_date, tags):
        """
        Constructs all the necessary attributes for the Metadata object
        :param filename: Path of the locations
        :param artist: Artist name
        :param song_name: Song Name
        :param release_date: Release date
        :param tags:List of tags
        """
        self.FileName = filename
        self.Artist = artist
        self.SongName = song_name
        self.ReleaseDate = release_date
        self.Tags = tags
