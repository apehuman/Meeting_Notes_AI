from datetime import datetime

from domain.note.note_schema import NoteCreate, NoteUpdate, NoteAI
from models import Folder, Note
from sqlalchemy.orm import Session


def get_notes(db: Session, folder_id):
    notes = db.query(Note)\
        .filter(Note.folder_id == folder_id)\
        .order_by(Note.date_added.desc())\
        .all()
    return notes


def get_note(db: Session, id: int):
    note = db.query(Note).get(id)
    return note


def create_note(db: Session, folder_id: Folder, note_create: NoteCreate):
    db_note = Note(folder_id=folder_id, 
                   topic=note_create.topic, 
                   content=note_create.content,
                   date_added=datetime.now())
    db.add(db_note)
    db.commit()


def update_note(db: Session, db_note: Note, note_update: NoteUpdate):
    db_note.topic = note_update.topic
    db_note.content = note_update.content
    db_note.date_edited = datetime.now()
    db.add(db_note)
    db.commit()


def update_note_ai_translation(db: Session, db_note: Note, note_ai_created: NoteAI):
    db_note.translation = note_ai_created.translation
    db.add(db_note)
    db.commit()


def update_note_ai_summary(db: Session, db_note: Note, note_ai_created: NoteAI):
    db_note.summary = note_ai_created.summary
    db.add(db_note)
    db.commit()


def update_note_ai_summary(db: Session, db_note: Note, note_ai_created: NoteAI):
    db_note.summary = note_ai_created.summary
    db.add(db_note)
    db.commit()


def update_note_ai_meeting_summary(db: Session, db_note: Note, note_ai_created: NoteAI):
    db_note.meeting_summary = note_ai_created.meeting_summary
    db.add(db_note)
    db.commit()