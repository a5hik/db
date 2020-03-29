
# books.py #
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Date
from db.base import Base
from sqlalchemy.dialects.postgresql import MONEY


@dataclass
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)
    published = Column(Date)
    price = Column(MONEY)

    def __repr__(self):
        return "<Book(title='{}', author='{}', pages={}, published={})>"\
                .format(self.title, self.author, self.pages, self.published)
