"""Functions related to server API call"""

import requests


def get_folders():
    folders_url = "http://127.0.0.1:8000/folder/list"
    return requests.get(folders_url).json()


def get_folder(folder_id):
    folder_url = f"http://127.0.0.1:8000/folder/{folder_id}"
    return requests.get(folder_url).json()


def create_folder(folder_name):
    folder_create_url = "http://127.0.0.1:8000/folder/create"
    return requests.post(folder_create_url, json={"name": folder_name})


def create_note(folder_id, topic, content):
    note_create_url = f"http://127.0.0.1:8000/note/create/{folder_id}"
    return requests.post(note_create_url, json={'topic': topic, 'content': content})