
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Proprieties import proprieties

engine = create_engine('postgresql://' +
                       proprieties.db_username + ':' +
                       proprieties.db_pass+'@localhost:' +
                       proprieties.db_port + '/postgres')

Session = sessionmaker(bind=engine)

Base = declarative_base()