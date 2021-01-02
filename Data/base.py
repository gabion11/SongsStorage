
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Proprieties import proprieties
try:
    # this is connection string for postgre database
    # engine = create_engine('postgresql://' +
    #                    proprieties.db_username + ':' +
    #                    proprieties.db_pass+'@localhost:' +
    #                    proprieties.db_port + '/postgres')
    # connection string for sqlite
    engine = create_engine(proprieties.sqlite_connection_string)
    Session = sessionmaker(bind=engine)
except ConnectionError:
    print("can't connect to database")

Base = declarative_base()