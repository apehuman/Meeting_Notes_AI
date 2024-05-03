import openai
import key         # file: OpenAI Client Key

openai.api_key = key.OPENAI_API_KEY   # Use your key
##############################################################################

def summarize_3lines(text, model="gpt-3.5-turbo"):
    """Summarize text into 3 lines of bullted points using gpt-3.5-turbo"""
    system_instruction = "Summarize content you are provided only into 3 lines of bulleted points"

    messages = [
        {
            "role": "system",
            "content": system_instruction,
        },
        {
            "role": "user",
            "content": text,
        },
    ]

    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        # max_tokens=64,
        top_p=1
    )
    result = response.choices[0].message.content
    return result
##############################################################################

def translate(text, src_lang, trg_lang, model="gpt-3.5-turbo"):
    """Translate text from source language into target language"""
    system_instruction = f"You will be provided with a sentence in {src_lang}, and your task is to translate it into {trg_lang}."

    messages = [
        {
            "role": "system",
            "content": system_instruction
        },
        {
            "role": "user",
            "content": text
        }
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
    """Chatbot generates response from user message"""
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
    )

    assistant_turn = response.choices[0].message
    return assistant_turn