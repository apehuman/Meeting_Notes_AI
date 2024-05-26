# Meeting_Notes_AI
AI Meeting Notes

## Table of Contents
* File/Directory Structure
   ```
    ├── main.py
    ├── database.py  (SQLAlchemy DB connection - SQLite)
    ├── models.py    (DB Modeling)
    ├── domain
    │   ├── folder
    │   ├── note
    │   ├── user
    │   ├── ai_text
    │   └── ai_audio
    └── front
        └──pages
    ```
* DB
   * Folder
        | Columns | Description |
        | ----------- | ----------- |
        | :white_check_mark: name        | 폴더명       |
        | :white_check_mark: date_added  | Timestamp   |
    * Note
        | Columns      | Description |
        | -----------  | ----------- |
        | :white_check_mark: topic        | 제목         |
        | :white_check_mark: content      | 메모/회의 내용 |
        | :white_check_mark: date_added   | Timestamp   |
        | :heavy_plus_sign: date_eidted   | Timestamp   |
        | :white_check_mark: folder_id    | 속한 folder (foreign key) |
        | attendee     | 참석자      |
        * Save & Load audio file
    * User
        | Columns | Description |
        | ----------- | ----------- |
        |  id       |  unique id (Primary key)       |
        |  name       | 이름        |


* AI Text
    | Function |          | URL      |
    | -------- | -------- | -------- | 
    |   요약   |  3줄 요약  | /summarize | 
    |         | 회의록 요약| /summarize-meeting| 
    |   번역    |         | /translate |
    | Chatbot |          | /chat     | 

    * 번역
        1.  text: source langauge -> target language
        2. text (source language detection) -> target language

---

## v0.1: AI Text - 요약, 번역, Chatbot
* **요약**: 3줄 요약 (/summarize)
* **번역**: Text + source language -> target language로 번역
* Chatbot: 현재 stream 방식이 아닌, batch style로 한 번에 응답하는 형태
## v0.2: AI Text - Update: 요약, 번역
1. **요약 - meeting note**: meeting note 형식에 적합한 요약 가능하도록 ai_text 함수 수정 및 API URL 추가 (/summarize-meeting)
    1. Overall summary
    2. Acition items
    3. Next Meeting Topics
2. **번역 - 언어 감지**: Text (source language) -> target language
    * 번역할 text에 target language만 주어져도, ChatGPT가 알아서 source language를 감지하여 번역할 수 있도록 API 호출 방식 추가 
    ```python
    # 기존 호출: 반드시 src_lang이 주어져야 함
    translated_text = translate(text, src_lang, trg_lang) 
    # 추가된 호출: keyword argument 사용하여 tar_lang만 제대로 지정하고, src_lang은 empty string으로 지정
    translated_text = translate(text, trg_lang="영어", src_lang="") 
    ```
3. minor errata fix (comments, typo)

---