from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.txt.declarative import declarative_base

engine = create_engine ('sqlite: ///atividades.db', convert_unicode = True)
db_session = scoped_session(sessionmaker(autocommit = False, binds = engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key = True)
    nome = Column(String(40), index = True)
    idade = Column(Integer)

    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key = True)
    nome = Column(String(80))
    