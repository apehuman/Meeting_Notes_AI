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
    """Summarize text into 3 lines."""
    summary = aitxt.summarize(input_text.text)
    return {"summary": summary}


@app.post("/summarize-meeting")
def post_summarize(input_text: InputText):
    """Summarize the meeting into 3 sections: 
    overall, action items, and next meeting topics"""
    meeting_summary = aitxt.summarize(input_text.text, meeting=True)
    return {"summary": meeting_summary}
##############################################################################

class TextTranslation(BaseModel):
    text: str
    src: str
    trg: str

@app.post("/translate")
def post_translate(translation: TextTranslation):
    """Translate text from source language into target language.
    Or it can detect source langauge from the given text 
    to tranlate into target language.
    """
    if translation.src:
        translation_text = aitxt.translate(translation.text, translation.trg, 
                                          src_lang=translation.src)
    else: 
        translation_text = aitxt.translate(translation.text, translation.trg)
    return {"translation": translation_text}
##############################################################################

class Turn(BaseModel):
    role: str
    content: str

class Messages(BaseModel):
    messages: List[Turn]

@app.post("/chat", response_model=Turn)
def post_chat(msgs: Messages):
    """Chatbot generates response from user's message."""
    msgs = dict(msgs)
    assistant_turn = aitxt.chat(msgs['messages'])
    return assistant_turn
##############################################################################