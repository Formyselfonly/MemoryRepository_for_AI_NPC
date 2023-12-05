import streamlit as st
import dotenv
from gpt_utils import openai_reply
from memory_repository import summary

def memoryrepository_talk(summary_and_forgetting_frequency):
    # 初始化会话状态变量
    if 'short_term_memory' not in st.session_state:
        st.session_state['short_term_memory'] = []
    if 'long_term_memory' not in st.session_state:
        st.session_state['long_term_memory'] = ""
    if 'round' not in st.session_state:
        st.session_state['round'] = 1

    metaprompt = "You're my assistant to help me!"
    user_input = st.text_input("input your message", key='user_input')

    if st.button("send"):
        prompt = metaprompt + st.session_state['long_term_memory'] + "".join(st.session_state['short_term_memory']) + user_input
        response = openai_reply(prompt)

        # 更新短期记忆
        st.session_state['short_term_memory'].append(f"user: {user_input}\nAI: {response}\n")

        # 更新长期记忆
        if st.session_state['round'] % summary_and_forgetting_frequency == 0:
            st.session_state['long_term_memory'] += summary("".join(st.session_state['short_term_memory']))
            st.session_state['short_term_memory'] = []

        st.session_state['round'] += 1

        # 显示当前对话的回答
        st.subheader("Local answer")
        st.write(f"AI: {response}")

        # 显示短期记忆
        st.subheader("Short-term memory")
        st.write("".join(st.session_state['short_term_memory']))

        # 显示长期记忆
        st.subheader("Long-term memory")
        st.write(st.session_state['long_term_memory'])

st.title('MemoryRepositoryDemo')
memoryrepository_talk(2)  # 设置您想要的频率
