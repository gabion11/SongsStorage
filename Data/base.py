
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Proprieties import proprieties
try:
    # engine = create_engine('postgresql://' +
    #                    proprieties.db_username + ':' +
    #                    proprieties.db_pass+'@localhost:' +
    #                    proprieties.db_port + '/postgres')
    engine = create_engine('sqlite:///C:/sqlite/sqlite-tools-win32-x86-3340000/storage.db')
    Session = sessionmaker(bind=engine)
except ConnectionError:
    print("can't connect to database")

Base = declarative_base()