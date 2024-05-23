from fastapi import FastAPI

from domain.folder import folder_router
from domain.note import note_router

app = FastAPI()


app.include_router(folder_router.router)
app.include_router(note_router.router)