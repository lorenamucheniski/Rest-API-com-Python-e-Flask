from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.txt.declarative import declarative_base

engine = create_engine ('sqlite: ///atividades.db', convert_unicode = True)
db_session = scoped_session(sessionmaker(autocommit = False, binds = engine))

Base = declarative_base()
Base.query = db_session.query_property()


