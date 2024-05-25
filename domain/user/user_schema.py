from pydantic import BaseModel, field_validator
from pydantic_core.core_schema import FieldValidationInfo

from domain.folder.folder_schema import Folder


class User(BaseModel):
    id: int
    username: str
    folders: list[Folder] = []

# class UserCreate(BaseModel):
#     username: str
#     password1: str
#     password2: str