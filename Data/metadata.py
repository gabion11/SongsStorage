from sqlalchemy import Column, String, Integer, Date

from Data.base import Base


class Metadate(Base):

    __tablename__ = 'metadata'

    Id = Column(Integer, primary_key=True)
    FileName = Column(String)
    Artist = Column(String)
    SongName = Column(String)
    ReleaseDate = Column(Date)
    Tags = Column(String)

    def __init__(self, filename, artist, song_name, release_date, tags):
        self.FileName = filename
        self.Artist = artist
        self.SongName = song_name
        self.ReleaseDate = release_date
        self.Tags = tags
