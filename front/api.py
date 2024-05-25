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
    note_update_url = f"http://127.0.0.1:8000/note/update"
    return requests.put(note_update_url, json={'id': note_id, 'topic': topic, 'content': content})

##############################################################################

def get_user_info(username):
    user_url = f"http://127.0.0.1:8000/user/{username}"
    return requests.get(user_url).json()