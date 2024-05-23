import datetime

from pydantic import BaseModel, field_validator

from domain.note.note_schema import Note


class Folder(BaseModel):
    id: int
    name: str
    date_added: datetime.datetime
    notes: list[Note] = []


class FolderCreate(BaseModel):
    name: str

    @field_validator('name')
    def is_valid(cls, v):
        if not v or not v.strip():
            raise ValueError('Invalid Input: Empty name')
        return v