from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from domain.folder.folder_schema import FolderCreate
from domain.note import note_crud
from models import Folder, User


def get_folders(db: Session):
    folders = db.query(Folder)\
            .order_by(Folder.date_added.desc())\
            .all()
    return folders


def get_folder(db: Session, id: int):
    folder = db.query(Folder).get(id)
    notes = note_crud.get_notes(db, id)
    folder.notes = notes
    return folder


def create_folder(db: Session, user: User, folder_create: FolderCreate):
    try: 
        db.query(Folder)\
            .filter(Folder.owner == user.id)\
            .filter(Folder.name == folder_create.name).one()
    except NoResultFound:
        db.rollback()
        db_folder = Folder(name=folder_create.name, 
                           date_added=datetime.now(),
                           owner=user.id)
        db.add(db_folder)
        db.commit()
    else:
        raise Exception("Duplicate Folder name")