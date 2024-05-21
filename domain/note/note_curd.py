from models import Note
from sqlalchemy.orm import Session


def get_notes(db: Session, folder_id):
    notes = db.query(Note)\
        .filter(Note.folder_id == folder_id)\
        .order_by(Note.date_added.desc())\
        .all()
    return notes
