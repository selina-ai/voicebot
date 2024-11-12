import streamlit as st
import openai
import numpy as np

# audiorecorder 패키지 추가
from audiorecorder import audiorecorder

## 메인 함수 ##
def main():
    st.set_page_config(
        page_title = "음성 비서 프로그램"
        )

# 제목
st.header("음성 비서 프로그램")

# 구분선
st.markdown("---")

# 기본 설명
with st.expander("음성비서 프로그램에 관하여", expanded=True):
    st.write(
        """
        - 음성 비서 프로그램의 UI는 스트림릿을 사용했습니다.
        - STT(Speech to Text)는 OpenAI의 Whisper AI를 활용했습니다.
        - 답변은 OpenAI의 GPT 모델을 활용했습니다.
        - TTS(Text-to-Speech)는 구글의 Google Translate TTS를 활용했습니다.
        """
    )

# 사이드바 생성
with st.sidebar:
    # Open AI API 키 입력받기
    openai.api_key = st.text_input(label="OPENAI API 키", placeholder="Enter Your API Key",
                                   value="", type="password")
    st.markdown("")

    # GPT 모델을 선택하기 위한 라디오 버튼 생성
    model = st.radio(label="GPT 모델", options=['gpt-4', 'gpt-3.5-turbo'])

    st.markdown("")

    # 리셋 버튼 생성
    if st.button(label="초기화"):
        # 리셋 코드
        st.session_state["chat"] = []
        st.session_state["messages"] = \
        [ {"role":"system", "content" : "You are a thoughtful assistant. Response to all input in 25 words and answer in korea"} ]
        st.session_state["check_audio"] = []

# 기능 구현 공간
col1,col2 = st.columns(2)
with col1:
    # 왼쪽 영역 작성
    st.subheader("질문하기")

    # session state 초기화
    if 'chat' not in st.session_state:
        st.session_state['chat'] = []
    
    if 'messages' not in st.session_state:
        st.session_state['messages'] = \
        [ {"role":"system", "content" : "You are a thoughtful assistant. Response to all input in 25 words and answer in korea"} ]
    
    if 'check_audio' not in st.session_state:
        st.session_state['check_audio'] = []

    # 음성 녹음 아이콘 추가
    audio = audiorecorder("클릭하여 녹음하기", "녹음 중...")
    if len(audio) > 0 and not np.array_equal(audio, st.session_state["check_audio"]):
        # 음성 재생
        st.audio(audio.export().read())

with col2:
    # 오른쪽 영역 작성
    st.subheader("질문/답변")