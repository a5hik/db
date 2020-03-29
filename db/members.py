# members.py #
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Date
from db.base import Base


@dataclass
class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    since = Column(Date)

    def __repr__(self):
        return "<Member(name='{}', type='{}', since={})>" \
            .format(self.name, self.type, self.since)
