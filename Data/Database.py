import sqlalchemy as db
import pandas as pd

class Metadate:
    def __init__(self):
        self.engine = db.create_engine('sqlite:///SongStorage') #Create test.sqlite automatically
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        self.emp = db.Table('Metadate',self.metadata,
              db.Column('Id', db.Integer()),
              db.Column('FileName', db.String(255), nullable=False),
              db.Column('Artist', db.String(255)),
              db.Column('SongName', db.String(255), nullable=False),
              db.Column("ReleaseDate", db.Date),
              db.Column("Tags", db.String(255))
              )

        self.metadata.create_all(self.engine) #Creates the table

    def insert_metadata(self, song_id, file_name, artist, song_name, release_date, tags ):
        query = db.insert(Metadate).values(Id=song_id, FileName=file_name, Artist=artist, SongName=song_name, ReleaseDate=release_date, Tags=tags, active=True)
        result = self.connection.execute(query)

    def get_data(self):
        results = self.connection.execute(db.select([Metadate])).fetchall()
        df = pd.DataFrame(results)
        df.columns = results[0].keys()
        df.head(4)

metadata = Metadate()
metadata.insert_metadata(1,"songstorage", "ionut", "la","12-02-2020", "#mood#iarna")
#metadata.get_data()
