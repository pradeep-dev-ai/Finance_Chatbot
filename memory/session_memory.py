import streamlit as st

def init_memory():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def add_to_memory(role, message):
    st.session_state.chat_history.append(
        {"role": role, "content": message}
    )

def get_chat_history():
    return st.session_state.chat_history
