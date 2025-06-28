import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key=api_key, model_name="gpt-4o-mini", temperature=0)

st.title("LLMチャットアプリ")

user_input = st.text_input("あなたのメッセージを入力してください:")

if user_input:
    messages = [
        SystemMessage(content="あなたは親切なアシスタントです。"),
        HumanMessage(content=user_input)
    ]
    response = llm(messages)
    st.write("AIの回答:", response.content)