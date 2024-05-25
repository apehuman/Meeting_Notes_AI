from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

import domain.ai_text.ai_text as aitxt

router = APIRouter(
    prefix="/ai-text",
)

##############################################################################

class InputText(BaseModel):
    text: str


@router.post("/summarize")
def post_summarize(input_text: InputText):
    """Summarize text into 3 lines."""
    summary = aitxt.summarize(input_text.text)
    return {"summary": summary}


@router.post("/summarize-meeting")
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


@router.post("/translate")
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


@router.post("/chat", response_model=Turn)
def post_chat(msgs: Messages):
    """Chatbot generates response from user's message."""
    msgs = dict(msgs)
    assistant_turn = aitxt.chat(msgs['messages'])
    return assistant_turn
##############################################################################