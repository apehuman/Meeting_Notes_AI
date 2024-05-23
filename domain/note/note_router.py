from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session

from database import get_db
from domain.folder import folder_crud
from domain.note import note_schema, note_crud

router = APIRouter(
    prefix="/note",
)


@router.post("/create/{folder_id}", status_code=status.HTTP_204_NO_CONTENT)
def note_create(folder_id: int, 
                _note_create: note_schema.NoteCreate,
                db: Session = Depends(get_db)):
    """Add a new note for a particular folder."""
    try: 
        folder_crud.get_folder(db, folder_id)
    except: 
        raise HTTPException(status_code=404, detail="Folder not found")
    else:
        note_crud.create_note(db, folder_id, _note_create)