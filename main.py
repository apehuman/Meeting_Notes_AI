from fastapi import FastAPI

from domain.folder import folder_router

app = FastAPI()


app.include_router(folder_router.router)