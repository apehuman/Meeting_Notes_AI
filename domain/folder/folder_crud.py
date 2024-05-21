from models import Folder
from sqlalchemy.orm import Session


def get_folder_list(db: Session):
    folder_list = db.query(Folder)\
            .order_by(Folder.date_added.desc())\
            .all()
    return folder_list
