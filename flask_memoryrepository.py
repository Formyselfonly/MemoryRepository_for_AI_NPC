import flask
from flask import request
from gpt_utils import openai_reply
from memory_repository import summary

server=flask.Flask(__name__)
server.config['JSON_AS_ASCII']=False

# 案例http://127.0.0.1:8080/memoryrepository_talk?txt=今日天气如何
# 调用是能调用,但是为什么 short-term-memory和long-term-memory都为空?
# 变量也不能更新
@server.route("/memoryrepository_talk",methods=["get","post"])
def translate():
    res = ""
    round = 1
    short_term_memory = [""]
    short_term_memory_str = ""
    long_term_memory_str = ""
    metaprompt = "You're my assistant to help me!"
    while True:
        print("-----Round{}-----\n".format(round))
        user_input = request.values.get("txt")
        print("------user_input------",user_input)
        print("------short_term_memory_str------",short_term_memory_str)
        prompt=metaprompt+long_term_memory_str+short_term_memory_str+user_input
        print("------prompt------", prompt)
        res=openai_reply(prompt)
        short_term_memory.append(user_input+res)
        short_term_memory_str=str(short_term_memory)
        if round%5==0:
            long_term_memory_str = summary(short_term_memory_str)
            short_term_memory_str=""
        print("------long_term_memory_str------",long_term_memory_str)
        print("------res------",res)
        round=round+1
        return res

if __name__=="__main__":
    server.run(debug=True,port=8080,host="0.0.0.0")