from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from database import get_db
from domain.user import user_schema, user_crud


router = APIRouter(
    prefix="/user",
)

@router.get("/{username}", response_model=user_schema.User)
def user(username: str, db: Session = Depends(get_db)):
    """Get all User info."""
    _user = user_crud.get_user(db, username)
    return _user