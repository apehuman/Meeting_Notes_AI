from passlib.context import CryptContext
from sqlalchemy.orm import Session

from domain.user.user_schema import UserCreatePasswd
from models import User, Folder


def get_user(db: Session, username: str):
    user = db.query(User).filter(User.username==username).one()
    user.folders = db.query(Folder)\
        .filter(Folder.owner==user.id)\
        .order_by(Folder.date_added.desc())\
        .all()
    return user


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user_create: UserCreatePasswd):
    db_user = User(username=user_create.username, 
                   password=pwd_context.hash(user_create.password1))
    db.add(db_user)
    db.commit()

def get_same_existing_user(db: Session, user_create: UserCreatePasswd):
    return db.query(User)\
        .filter(User.username==user_create.username)\
        .first()