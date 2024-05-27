from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=True)

    folders = relationship("Folder", backref="user", cascade='all, delete')

# Create your models here
class Folder(Base):
    """A folder contains meeting notes"""
    __tablename__ = "folders"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date_added = Column(DateTime, nullable=False)
    owner = Column(Integer, ForeignKey("users.id"), nullable=True)

    notes = relationship("Note", backref="folder", cascade='all, delete')  # 1:M relationship; cascade delete


class Note(Base):
    """Meeting Notes"""
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    topic = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    date_added = Column(DateTime, nullable=False)
    date_edited = Column(DateTime, nullable=True)
    translation = Column(Text, nullable=True)
    summary = Column(Text, nullable=True)
    meeting_summary = Column(Text, nullable=True)
    folder_id = Column(Integer, ForeignKey("folders.id"))
    # TODO: attendee = 