from datetime import datetime
from sqlalchemy import Column, String, Integer, Text, Date, ForeignKey

import sys
sys.path = ['','..'] + sys.path[1:]

from db.base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    fio = Column(Text)
    datar = Column(Date)
    id_role = Column(Integer, ForeignKey('roles.id'))


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))