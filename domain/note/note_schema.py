import datetime

from pydantic import BaseModel


class Note(BaseModel):
    id: int
    topic: str
    content: str
    date_added: datetime.datetime