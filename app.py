import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

import os
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# LLM設定（GPT-4o miniを使用）
llm = ChatOpenAI(openai_api_key=api_key, model_name="GPT-4o mini", temperature=0)

# ▼ 関数：専門家の種類と入力テキストを受け取り、LLMから回答を得る
def generate_response(role: str, user_input: str) -> str:
    # 専門家の役割に応じたSystemメッセージ
    system_message = f"You are a helpful expert in the field of {role}."

    # 会話メッセージのリスト
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_input)
    ]

    response = llm(messages)
    return response.content

# ▼ Streamlit UI構成
st.title("専門家LLMチャットアプリ 🤖💬")
st.write("このアプリでは、さまざまな専門家に質問をして回答を得ることができます。以下の手順で操作してください：")
st.markdown("""
1. 専門家の分野を選択
2. 質問を入力
3. 「送信」をクリック
""")

# 専門家の種類（必要に応じて追加可能）
expert_roles = ["健康", "法律", "旅行", "歴史", "テクノロジー"]
selected_role = st.radio("専門家の種類を選択してください：", expert_roles)

# ユーザーの入力
user_question = st.text_input("質問を入力してください：")

# ボタンで送信処理
if st.button("送信"):
    if user_question.strip() == "":
        st.warning("質問を入力してください。")
    else:
        with st.spinner("専門家が考え中..."):
            answer = generate_response(selected_role, user_question)
            st.success("回答：")
            st.write(answer)