from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from domain.folder.folder_schema import FolderCreate
from domain.note import note_curd
from models import Folder


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


def create_folder(db: Session, folder_create: FolderCreate):
    db_folder = Folder(name=folder_create.name)
    try: 
        db.add(db_folder)
        db.flush()
    except IntegrityError:
        db.rollback()
        raise Exception("Duplicate folder name")
    else:
        db.commit()