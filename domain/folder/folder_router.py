from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db # SessionLocal
from domain.folder import folder_schema, folder_crud
from models import Folder

router = APIRouter(
    prefix="/folder",
)

@router.get("/list", response_model=list[folder_schema.Folder])
def folder_list(db: Session = Depends(get_db)):   # Dependency Injection
    """Show all folders"""
    _folder_list = folder_crud.get_folder_list(db)
    return _folder_list
