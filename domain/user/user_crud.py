from sqlalchemy.orm import Session

from models import User


def get_user(db: Session, username: str):
    user = db.query(User).filter(User.username==username).one()
    return user