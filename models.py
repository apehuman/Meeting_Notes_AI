from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


# Create your models here
class Folder(Base):
    """A folder contains meeting notes"""
    __tablename__ = "folders"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    date_added = Column(DateTime, nullable=False, default=datetime.now())

    notes = relationship("Note", backref="folder", cascade='all, delete')  # 1:M relationship; cascade delete

class Note(Base):
    """Meeting Notes"""
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    topic = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    date_added = Column(DateTime, nullable=False, default=datetime.now())
    folder_id = Column(Integer, ForeignKey("folders.id"))
    # TODO: attendee = 