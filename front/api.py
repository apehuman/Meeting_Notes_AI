"""Functions related to server API call"""

import requests


def get_folders():
    folders_url = "http://127.0.0.1:8000/folder/list"
    return requests.get(folders_url).json()

def get_folder(folder_id):
    folder_url = f"http://127.0.0.1:8000/folder/{folder_id}"
    return requests.get(folder_url).json()

def create_folder(folder_name, username):
    folder_create_url = f"http://127.0.0.1:8000/folder/create/{username}"
    return requests.post(folder_create_url, json={"name": folder_name})

##############################################################################

def get_note(note_id):
    note_url = f"http://127.0.0.1:8000/note/{note_id}"
    return requests.get(note_url).json()


def create_note(folder_id, topic, content):
    note_create_url = f"http://127.0.0.1:8000/note/create/{folder_id}"
    return requests.post(note_create_url, json={'topic': topic, 'content': content})


def update_note(note_id, topic, content):
    note_update_url = "http://127.0.0.1:8000/note/update"
    return requests.put(note_update_url, json={'id': note_id, 'topic': topic, 'content': content})

# ----------- ----------- ----------- ----------- ----------- ----------- ----
# AI

def update_note_translation(note_id, translation):
    url = "http://127.0.0.1:8000/note/update-ai-translation"
    return requests.put(url, json={'id': note_id, 'translation': translation})

def update_note_summary(note_id, summary):
    url = "http://127.0.0.1:8000/note/update-ai-summary"
    return requests.put(url, json={'id': note_id, 'summary': summary})

def update_note_meeting_summary(note_id, summary):
    url = "http://127.0.0.1:8000/note/update-ai-meeting"
    return requests.put(url, json={'id': note_id, 'meeting_summary': summary})
##############################################################################

def get_user_info(username):
    user_url = f"http://127.0.0.1:8000/user/{username}"
    return requests.get(user_url).json()

def create_user(username, pwd1, pwd2):
    user_create_url = "http://127.0.0.1:8000/user/create"
    return requests.post(user_create_url, json={'username': username, 
                                                'password1': pwd1, 'password2': pwd2})

def user_login(username, pwd):
    user_login_url = "http://127.0.0.1:8000/user/login"
    return requests.post(user_login_url, json={'username': username, 'password': pwd})
