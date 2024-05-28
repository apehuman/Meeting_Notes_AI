"""Functions related to Basic AI Text"""

import openai
import key         # file: OpenAI Client Key

openai.api_key = key.OPENAI_API_KEY   # Use your own key
##############################################################################

def summarize(text, model="gpt-3.5-turbo", meeting=False):
    """Summarize text into 3 lines of bullted points"""
    """Summarize the meeting into 3 sections: 
    overall, action items, and next meeting topics
    """
    if meeting:
        # system_instruction = """
        # You will be provided with meeting notes, and your task is to summarize the meeting as follows:
        
        # -Overall summary of discussion
        # -Action items (what needs to be done and who is doing it)
        # -If applicable, a list of topics that need to be discussed more fully in the next meeting.

        # Don't forget to speak in Korean.
        # """
        system_instruction = """
        너에게 회의록이 주어질 텐데, 너의 업무는 이 회의록을 다음과 같이 요약하는거야:

        - 회의 전체 요약
        - 액션 아이템 (무엇이 행해져야하고, 누가 하고 있는지)
        - 다음 회의에 논의되어야 할 주제들
        """
    else:
        system_instruction = "Summarize content you are provided only into 3 lines of bulleted points"

    messages = [
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": text},
    ]

    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.3,
        # max_tokens=64,
        top_p=1
    )
    result = response.choices[0].message.content
    return result
##############################################################################

def translate(text, trg_lang, model="gpt-3.5-turbo", src_lang=''):
    """Translate text from source language into target language.
    Or it can detect the source language, 
    so you can translate only with the target language.
    """
    if src_lang:
        system_instruction = f"You will be provided with a sentence in {src_lang}, and your task is to translate it into {trg_lang}."
    else:
        system_instruction = "You will be provided the text, and your task is to detect the source language and translate it into a given target language."
        system_instruction += f"\nTranslate this into {trg_lang}: {text}"

    messages = [
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": text},
    ]

    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        # max_tokens=64,
        top_p=1
    )

    translated_text = response.choices[0].message.content
    return translated_text
##############################################################################

def chat(messages, model="gpt-3.5-turbo"):
    """Chatbot generates response from user message."""
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
    )

    assistant_turn = response.choices[0].message
    return assistant_turn