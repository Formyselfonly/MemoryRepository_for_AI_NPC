from flask import Flask, request
from gpt_utils import openai_reply
from memory_repository import summary

app = Flask(__name__)

short_term_memory = []  # 全局变量保存 short_term_memory
short_term_memory_str = ""
long_term_memory_str = ""
round = 1

# How to Start?
#1.Run Project
#2.click on http://127.0.0.1:8080 to open
#3.Test
#3.1  http://127.0.0.1:8080/memoryrepository_talk?txt="What's the weather in London weather?"
#3.2 http://127.0.0.1:8080/memoryrepository_talk?txt="What should i wear?"
#3.3 http://127.0.0.1:8080/memoryrepository_talk?txt="Thanks"
#3.4 Look at the output printed by the console
# And You can see How the MemoryRepository act

@app.route("/memoryrepository_talk", methods=["get", "post"])
def talk():
    global short_term_memory  # 声明全局变量
    global short_term_memory_str  # 声明全局变量
    global long_term_memory_str  # 声明全局变量
    global round  # 声明全局变量
    res = ""

    metaprompt = "You're my assistant to help me!"
    user_input = request.values.get("txt")
    print("-----Round{}-----\n".format(round))
    print("------user_input------", user_input)
    print("------short_term_memory_str------", short_term_memory_str)
    prompt = metaprompt + long_term_memory_str + short_term_memory_str + user_input
    print("------prompt------", prompt)
    res = openai_reply(prompt)
    short_term_memory.append(user_input + res)
    short_term_memory_str = str(short_term_memory)
    # Change to 5 for production environment
    if round % 2 == 0:
        long_term_memory_str = summary(short_term_memory_str)
        short_term_memory_str = ""
    print("------long_term_memory_str------", long_term_memory_str)
    print("------res------", res)
    round = round + 1
    return res

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")