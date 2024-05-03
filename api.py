from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

import ai_text as aitxt


app = FastAPI()
##############################################################################

class InputText(BaseModel):
    text: str

@app.post("/summarize")
def post_summarize(input_text: InputText):
    summary = aitxt.summarize_3lines(input_text.text)
    return {"summary": summary}
##############################################################################

class TextTranslation(BaseModel):
    text: str
    src: str
    trg: str

@app.post("/translate")
def post_translate(translation: TextTranslation):
    translation_text = aitxt.translate(translation.text, translation.src, translation.trg)
    return {"translation": translation_text}
##############################################################################

class Turn(BaseModel):
    role: str
    content: str

class Messages(BaseModel):
    messages: List[Turn]

@app.post("/chat", response_model=Turn)
def post_chat(msgs: Messages):
    msgs = dict(msgs)
    assistant_turn = aitxt.chat(msgs['messages'])
    return assistant_turn
##############################################################################
