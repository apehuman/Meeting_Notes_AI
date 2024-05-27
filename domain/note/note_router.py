from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session

from database import get_db
from domain.folder import folder_crud
from domain.note import note_schema, note_crud

router = APIRouter(
    prefix="/note",
)


@router.get("/{note_id}", response_model=note_schema.Note)
def note(note_id: int, db: Session = Depends(get_db)):
    _note = note_crud.get_note(db, note_id)
    return _note


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


@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def note_update(_note_update: note_schema.NoteUpdate,
                db: Session = Depends(get_db)):
    """Edit an existing note."""
    db_note = note_crud.get_note(db, _note_update.id)
    if not db_note:
        raise HTTPException(status_code=404, detail="That note doesn't exist.")
    note_crud.update_note(db, db_note, _note_update)

#-----------------------------------------------------------------

@router.put("/update-ai-translation", status_code=status.HTTP_204_NO_CONTENT)
def note_update_ai(_note_update_ai: note_schema.NoteAI,
                   db: Session = Depends(get_db)):
    """Add a new AI contents in the note: translation"""
    db_note = note_crud.get_note(db, _note_update_ai.id)
    if not db_note:
        raise HTTPException(status_code=404, detail="That note doesn't exist.")
    note_crud.update_note_ai_translation(db, db_note, _note_update_ai)


@router.put("/update-ai-summary", status_code=status.HTTP_204_NO_CONTENT)
def note_update_ai(_note_update_ai: note_schema.NoteAI,
                   db: Session = Depends(get_db)):
    """Add a new AI contents in the note: summary"""
    db_note = note_crud.get_note(db, _note_update_ai.id)
    if not db_note:
        raise HTTPException(status_code=404, detail="That note doesn't exist.")
    note_crud.update_note_ai_summary(db, db_note, _note_update_ai)


@router.put("/update-ai-meeting", status_code=status.HTTP_204_NO_CONTENT)
def note_update_ai_meeting(_note_update_ai: note_schema.NoteAI,
                   db: Session = Depends(get_db)):
    """Add a new AI contents in the note: summary"""
    db_note = note_crud.get_note(db, _note_update_ai.id)
    if not db_note:
        raise HTTPException(status_code=404, detail="That note doesn't exist.")
    note_crud.update_note_ai_meeting_summary(db, db_note, _note_update_ai)
