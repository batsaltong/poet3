import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 환경 변수 로드
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# OpenAI 모델 설정
chat_model = ChatOpenAI(openai_api_key=api_key)

# Streamlit UI 구성
st.title("AI시 생성기")
st.write("주제를 입력하면 AI가 맛있는 시를 호로록!")

# 사용자 입력 받기
jujae = st.text_input("주제를 입력해주세요.")
person = st.text_input("원하는 스타일의 시인을 입력하세요")
julgle = st.text_input("몇줄이내로 써드릴까요?")

prompt = f"{jujae}를 주제로 시를 써줄래, {person} 느낌으로 해줘, {julgle}이내로 써줄래?."

# "시 생성" 버튼을 추가
if st.button("시 생성"):
    if not jujae:
        st.error("주제를 입력해주세요!")
    else:
        try:
            response = chat_model.invoke(prompt)
            st.subheader("생성된 시")
            st.write(response.content)
        except Exception as e:
            st.error(f"오류 발생: {e}")