from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session

from database import get_db # SessionLocal
from domain.folder import folder_schema, folder_crud
from domain.user import user_crud

router = APIRouter(
    prefix="/folder",
)


@router.get("/list", response_model=list[folder_schema.Folder])
def folders(db: Session = Depends(get_db)):   # Dependency Injection
    """Show all folders."""
    _folders = folder_crud.get_folders(db)
    return _folders


@router.get("/{folder_id}", response_model=folder_schema.Folder)
def folder(folder_id: int, 
           db: Session = Depends(get_db)):   # Dependency Injection
    """Show a single folder and all its notes."""
    _folder = folder_crud.get_folder(db, id=folder_id)
    return _folder


@router.post("/create/{username}", status_code=status.HTTP_204_NO_CONTENT) # Success: no return output
def folder_create(username: str,
                  _folder_create: folder_schema.FolderCreate,
                  db: Session = Depends(get_db)):
    """Add a new folder."""
    user = user_crud.get_user(db, username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    try:
        folder_crud.create_folder(db, user, _folder_create)
    except:
        raise HTTPException(status_code=404, detail="Duplicate Folder name")