def extract_transcription(json_data):
    # 발화 내용 추출
    transcriptions = [utterance['msg'] for utterance in json_data['results']['utterances']]
    
    # 발화 내용을 하나의 문자열로 합치기
    transcriptions_combined = ' '.join(transcriptions)
    
    return transcriptions_combined

def audio_process(file_name):
  import json
  import requests
  import time
  #----------------------------------------Authentication 부분----------------------------------------------#
  resp_accesstoken = requests.post(
      'https://openapi.vito.ai/v1/authenticate',
      data={'client_id': 'QfW9JoCJMVL7-Fr51j6R', #사용시마다 재발급 받아야 함
            'client_secret': 'KgAZ_pDI7T9IQJblPkiBUkjaWfy2ZCOsygqnKk35'}
  )
  resp_accesstoken.raise_for_status()

  tokenresponse_json = resp_accesstoken.json()  # JSON 응답을 딕셔너리로 변환

  # print(response_json)

  # JSON 응답에서 'access_token' 값 추출
  access_token = tokenresponse_json['access_token']

  # print('access token is : '+access_token) #access_token 값에 앞으로 계속 사진의 토큰을 저장함

  #------------------------------------------stt 환경설정----------------------------------------------------#
  config = {
    "use_diarization": True,
    "diarization": {
      "spk_count": 2
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
  #-------------------------------------------stt 전사요청 부분----------------------------------------------#
  resp_sttAIresponseID = requests.post(
      'https://openapi.vito.ai/v1/transcribe',
      headers={'Authorization': 'bearer '+ access_token}, #자기 토큰
      data={'config': json.dumps(config)},
      files= {'file': file_name}
      #files={'file': open(file_name, 'rb')}   #전사요청할 음성파일 이름
  )

  resp_sttAIresponseID.raise_for_status()
  #print(resp_sttAIresponseID.json())

  IDresponse_json = resp_sttAIresponseID.json()  # JSON 응답을 딕셔너리로 변환

  # JSON 응답에서 'access_token' 값 추출
  ID = IDresponse_json['id']
  print('response id is :' + ID)  # ID값은 전사요청 파일의 ID -> 고유 ID값으로 데이터베이스에 저장? 혹은 다른 방법을 사용할수도

  #print(ID)

  #----------------------------------------------전사요청 결과 조회------------------------------------------#
  while True:
    resp_sttResult = requests.get(
        'https://openapi.vito.ai/v1/transcribe/'+ID,
      headers={'Authorization': 'bearer ' + access_token}
    )
    resp_sttResult.raise_for_status()
    response_json = resp_sttResult.json()
    
    if response_json['status'] == 'completed':  # 전사가 완료될때까지 요청을 하고, 아직 전사중이라면 5초뒤 재요청
        resp_sttResult.raise_for_status()
        print("전사결과:")
        print(resp_sttResult.json())
        print("추출문:"+ extract_transcription(resp_sttResult.json()))
        return(extract_transcription(resp_sttResult.json()))
    elif response_json['status'] == 'transcribing':
        print(f"File ID: {ID}, Transcription is still in progress. Waiting for 5 seconds...")
        time.sleep(5)