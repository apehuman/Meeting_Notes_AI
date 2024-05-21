from models import Folder
from sqlalchemy.orm import Session
from domain.note import note_curd


def get_folders(db: Session):
    folders = db.query(Folder)\
            .order_by(Folder.date_added.desc())\
            .all()
    return folders


def get_folder(db: Session, id: int):
    folder = db.query(Folder).get(id)
    notes = note_curd.get_notes(db, id)
    folder.notes = notes
    return folder