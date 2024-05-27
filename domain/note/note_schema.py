import datetime

from pydantic import BaseModel, field_validator


class Note(BaseModel):
    id: int
    topic: str
    content: str
    date_added: datetime.datetime
    date_edited: datetime.datetime | None = None
    translation: str | None = None
    summary: str | None = None
    meeting_summary: str | None = None

class NoteCreate(BaseModel):
    topic: str
    content: str

    @field_validator('topic', 'content')
    def is_valid(cls, v):
        if not v or not v.strip():
            raise ValueError('Invalid Input: Empty value')
        return v


class NoteUpdate(NoteCreate):
    id: int


class NoteAI(BaseModel):
    id: int
    translation: str | None = None
    summary: str | None = None
    meeting_summary: str | None = None