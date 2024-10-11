import streamlit as st
import dotenv
from gpt_utils import npc_reply
from memory_repository import summary

def memoryrepository_talk(summary_and_forgetting_frequency):
    # 初始化会话状态变量
    if 'short_term_memory' not in st.session_state:
        st.session_state['short_term_memory'] = []
    if 'long_term_memory' not in st.session_state:
        st.session_state['long_term_memory'] = ""
    if 'round' not in st.session_state:
        st.session_state['round'] = 1
    metaprompt = "You're Darth Vader,here i your description:https://en.wikipedia.org/wiki/Darth_Vader"
    user_input = st.text_input("input your message", key='user_input')

    if st.button("send"):
        prompt = metaprompt + st.session_state['long_term_memory'] + "".join(st.session_state['short_term_memory']) + user_input
        response = npc_reply(prompt)

        # 更新短期记忆
        st.session_state['short_term_memory'].append(f"user: {user_input}\nNPC: {response}\n")
        st.session_state['talk_history'].append(f"user: {user_input}\n NPC: {response}\n","----------")


        # 更新长期记忆
        if st.session_state['round'] % summary_and_forgetting_frequency == 0:
            st.session_state['long_term_memory'] += summary("".join(st.session_state['short_term_memory']))
            st.session_state['short_term_memory'] = []

        st.session_state['round'] += 1

        # 显示当前对话的回答
        st.subheader("Local answer")
        st.write(f"NPC: {response}")

        # 显示短期记忆
        st.subheader("Talk History")
        st.write("".join(st.session_state['talk_history']))



st.title('MemoryRepository Experiment')
memoryrepository_talk(3)  # 设置您想要的频率
