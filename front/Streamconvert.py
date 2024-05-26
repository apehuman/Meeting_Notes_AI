import streamlit as st
from st_audiorec import st_audiorec
import audio_process

# Streamlit 앱의 제목
st.title("녹음 변환기")

if 'conversion_result' not in st.session_state:
    st.session_state['conversion_result'] = "변환 결과가 여기에 표시됩니다."
#녹음중
wav_audio_data = st_audiorec()

# 변환 버튼
if st.button("변환",key="convert_button"):
    
    st.session_state['conversion_result'] = audio_process.audio_process(wav_audio_data)

# 변환 결과를 텍스트 박스에 출력
st.subheader("변환 결과")
st.text_area("conversion_result",value=st.session_state['conversion_result'], height=360 , label_visibility= "hidden")

# 초기화 버튼
if st.button("초기화"):
    st.session_state['conversion_result'] = "변환 결과가 여기에 표시됩니다."
    st.session_state.button_clicked = False
    st.experimental_rerun()


# Session state를 사용하여 버튼 클릭 상태를 저장
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

# 버튼 클릭 이벤트 처리
def on_button_click():
    st.session_state.button_clicked = True

# 버튼을 클릭했는지 확인
if st.button('저장', on_click=on_button_click):
    st.session_state.button_clicked = True

# 버튼 클릭 후 텍스트 입력 필드와 입력값 처리
if st.session_state.button_clicked:
    title = st.text_input('제목을 입력하세요:', on_change=None)
    if title:
        st.write(f'입력한 제목: {title}')
        #제목값은 title , 전사 결과는 st.session_state['conversion_result']