from sqlalchemy.orm import Session

from models import User, Folder


def get_user(db: Session, username: str):
    user = db.query(User).filter(User.username==username).one()
    user.folders = db.query(Folder)\
        .filter(Folder.owner==user.id)\
        .order_by(Folder.date_added.desc())\
        .all()
    return user