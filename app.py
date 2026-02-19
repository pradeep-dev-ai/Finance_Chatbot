import streamlit as st
from services.gemini_service import GeminiService
from memory.session_memory import init_memory, add_to_memory, get_chat_history
from prompts.financial_prompts import build_prompt

st.set_page_config(page_title="Financial Advisor Chatbot")

st.title("Financial Advisor Chatbot")

init_memory()

gemini = GeminiService()

user_input = st.chat_input("Ask your financial question...")

if user_input:
    add_to_memory("user", user_input)

    prompt = build_prompt(user_input, get_chat_history())
    response = gemini.generate_response(prompt)

    add_to_memory("assistant", response)

for message in get_chat_history():
    with st.chat_message(message["role"]):
        st.write(message["content"])
