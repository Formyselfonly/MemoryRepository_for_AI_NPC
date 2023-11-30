from wxauto import *
from tkinter import ttk
import tkinter as tk
import time
import openai
import requests
import re


# 检查桌面微信客户端
wx=WeChat()
wx.GetSessionList()

# 设置参数变量
who="For"
wx.ChatWith(who)
wx.SendMsg("你在赣什么?@我然后和我对话")
bot=wx.GetLastMessage[0]
print(">>>>>>>>>>>>")
print("机器人名:"+bot)
print("作用对象:"+who)
print("<<<<<<<<<<<<")

def openai_reply(content, apikey):
    openai.api_key = apikey
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",  # gpt-3.5-turbo-0301
        messages=[
            {"role": "user", "content": content}
        ],
        temperature=0.5,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    # print(response)
    return response.choices[0].message.content

# 运行微信机器人
while True:
    msgs=wx.GetLastMessage[1]
    prompt="".join(str(i) for i in re.findall("@"+bot+'(.*)',str(msgs)))
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~"+prompt)
    if prompt!="":
        response=openai_reply(prompt,"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")
        print(response)
        msg=response
        WxUtils.SetClipboard(msg)
        wx.SendClipboard()
        time.sleep(1)
