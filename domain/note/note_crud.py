from models import Note
from sqlalchemy.orm import Session

from domain.note.note_schema import NoteCreate
from models import Folder, Note


def get_notes(db: Session, folder_id):
    notes = db.query(Note)\
        .filter(Note.folder_id == folder_id)\
        .order_by(Note.date_added.desc())\
        .all()
    return notes


def create_note(db: Session, folder_id: Folder, note_create: NoteCreate):
    db_note = Note(folder_id=folder_id, 
                   topic=note_create.topic, content=note_create.content)
    db.add(db_note)
    db.commit()