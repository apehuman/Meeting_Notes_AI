from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status


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

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create: user_schema.UserCreatePasswd, db: Session = Depends(get_db)):
    user = user_crud.get_same_existing_user(db, _user_create)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="이미 존재하는 사용자입니다.")
    user_crud.create_user(db, _user_create)