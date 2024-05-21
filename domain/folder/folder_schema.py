import datetime

from pydantic import BaseModel

from domain.note.note_schema import Note


class Folder(BaseModel):
    id: int
    name: str
    date_added: datetime.datetime
    notes: list[Note] = []