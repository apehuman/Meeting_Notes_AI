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
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="이미 존재하는 사용자입니다.")

    try:
        user = user_crud.create_user(db, _user_create)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return user


@router.post("/login", status_code=status.HTTP_200_OK)
def user_login(_existing_user: user_schema.UserLogin, db: Session = Depends(get_db)):
    user = user_crud.get_existing_user(db, _existing_user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="존재하지 않는 사용자입니다: id-pwd 불일치")
