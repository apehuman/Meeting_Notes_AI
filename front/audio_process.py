import json
import requests
import time


def extract_transcription(json_data):
    # 발화 내용 추출
    transcriptions = [utterance['msg']
                      for utterance in json_data['results']['utterances']]

    # 발화 내용을 하나의 문자열로 합치기
    transcriptions_combined = ' '.join(transcriptions)

    return transcriptions_combined


def extract_conversation(json_data):
    # 발화 내용 추출
    transcriptions = [f"발화자 {utterance['spk']} : {utterance['msg']}\n" for utterance in json_data['results']['utterances']]

    # 발화 내용을 하나의 문자열로 합치기
    transcriptions_combined = ''.join(transcriptions)

    return transcriptions_combined


def audio_process(file_name, mode='transcription'):
    # 인증 부분
    resp_accesstoken = requests.post(
        'https://openapi.vito.ai/v1/authenticate',
        data={
            'client_id': 'QfW9JoCJMVL7-Fr51j6R',  # 사용시마다 재발급 받아야 함
            'client_secret': 'KgAZ_pDI7T9IQJblPkiBUkjaWfy2ZCOsygqnKk35'
        }
    )
    resp_accesstoken.raise_for_status()
    tokenresponse_json = resp_accesstoken.json()
    access_token = tokenresponse_json['access_token']

    # STT 환경설정
    config = {
        "use_diarization": True,
        "diarization": {
            "spk_count": 6
        },
        "use_multi_channel": False,
        "use_itn": False,
        "use_disfluency_filter": False,
        "use_profanity_filter": False,
        "use_paragraph_splitter": True,
        "paragraph_splitter": {
            "max": 50
        }
    }

    # STT 전사요청
    resp_sttAIresponseID = requests.post(
        'https://openapi.vito.ai/v1/transcribe',
        headers={'Authorization': 'bearer ' + access_token},
        data={'config': json.dumps(config)},
        files={'file': file_name}
    )
    resp_sttAIresponseID.raise_for_status()
    IDresponse_json = resp_sttAIresponseID.json()
    ID = IDresponse_json['id']
    print('response id is :' + ID)

    # 전사요청 결과 조회
    while True:
        resp_sttResult = requests.get(
            'https://openapi.vito.ai/v1/transcribe/' + ID,
            headers={'Authorization': 'bearer ' + access_token}
        )
        resp_sttResult.raise_for_status()
        response_json = resp_sttResult.json()

        if response_json['status'] == 'completed':
            print("전사결과:")
            print(resp_sttResult.json())
            if mode == 'transcription':
                print("추출문:" + extract_transcription(resp_sttResult.json()))
                return extract_transcription(resp_sttResult.json())
            elif mode == 'conversation':
                print("회의록:" + extract_conversation(resp_sttResult.json()))
                return extract_conversation(resp_sttResult.json())

        elif response_json['status'] == 'transcribing':
            print(f"File ID: {
                  ID}, Transcription is still in progress. Waiting for 5 seconds...")
            time.sleep(5)
        elif response_json['status'] == 'failed':
            print("error , transcribing failed")
            break