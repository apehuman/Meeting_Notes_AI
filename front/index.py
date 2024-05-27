import streamlit as st
import template

template.base()

# 사이트 제목
st.title("SOUNDSCAN")
st.write("Tracking your Meeting Notes.")
st.write("AI-powered STT with text summary & translation.")
st.write("##")
st.markdown('<div style="margin: 40px;"></div>', unsafe_allow_html=True)
# 녹음 파일 텍스트 변환 및 실시간 음성 변환 버튼 나란히 배치
col1, col2, col3, col4 = st.columns([0.5, 3, 0.5, 3])

with col1:
    st.write("##")

with col2:
    st.image("img/headphone.png", width=150)
    st.markdown('<div style="margin: 28px;"></div>', unsafe_allow_html=True)
    if st.button('음성녹음 파일 변환'):
        st.switch_page("pages/Fileconvert.py")

with col3:
    st.write("##")

with col4:
    st.image("img/file.png", width=160)
    st.markdown('<div style="margin: 1px;"></div>', unsafe_allow_html=True)
    if st.button('실시간 음성 변환'):
        st.switch_page("pages/Streamconvert.py")

# 디스코드 플러그인 다운로드 섹션
st.write("##")
st.write("##")
st.subheader("디스코드 플러그인")
col1, col2 = st.columns([3, 2])
with col1:
    st.write("##")
    st.markdown("<div style='padding-left:20px;'>▶ 음성 채팅을 실시간으로 기록</div>", unsafe_allow_html=True)
    st.markdown('<div style="margin: 20px;"></div>', unsafe_allow_html=True)
    st.markdown("<div style='padding-left:20px;'>▶ 회의 기록을 조금 더 쉽게</div>", unsafe_allow_html=True)
    st.write("##")
    st.markdown('<div style="margin: 40px;"></div>', unsafe_allow_html=True)
    st.write("디스코드 플러그인 다운로드는 아래 버튼 클릭")
    st.button("다운로드")
with col2:
    st.image("img/computer.jpg") # 이미지 경로를 실제 경로로 변경해야 합니다.

# 푸터 추가
st.write("---")
st.write("© 2024 SOUNDSCAN. All rights reserved.")