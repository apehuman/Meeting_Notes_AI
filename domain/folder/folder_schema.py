import datetime

from pydantic import BaseModel


class Folder(BaseModel):
    id: int
    name: str
    date_added: datetime.datetime

