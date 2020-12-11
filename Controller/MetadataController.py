from Data.metadata import Metadate
from Data.base import Session, engine, Base

Base.metadata.create_all(engine)


class MetadataController:

    def __init__(self):
        self.session = Session()

    def insert_metadata(self, filename, artist, song_name, release_date, tags):
        song1 = Metadate(filename, artist, song_name, release_date, tags)
        self.session.add(song1)
        self.session.commit()
        return song1.Id

    def get_all_metadata(self):
        songs = self.session.query(Metadate).all()
        return songs

    def delete_metadata(self, _id):
        self.session.query(Metadate).filter_by(Id=_id).delete()
        self.session.commit()

    def get_metadata(self, artist):
        q = self.session.query(Metadate)
        for attr, value in artist.items():
            q = q.filter(getattr(Metadate, attr).like("%%%s%%" % value))
        return q

    def get_by_id(self, _id):
        song = self.session.query(Metadate).get(_id)
        return song

    def update_metadata(self, _id, metadate):
        self.session.query(Metadate).filter(Metadate.Id == _id).update(metadate, synchronize_session=False)
        self.session.commit()
        return self.get_by_id(_id)

    @staticmethod
    def print_metadata(meta):
        print(f'{meta.Id}  {meta.FileName}    {meta.Artist}    {meta.SongName}    {meta.ReleaseDate}    {meta.Tags} ')
