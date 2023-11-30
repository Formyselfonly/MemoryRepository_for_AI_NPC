import dotenv
from gpt_utils import openai_reply
from memory_repository import summary

def memoryrepository_talk(summary_and_forgetting_frequence):
    res = ""
    round = 1
    short_term_memory = [""]
    short_term_memory_str = ""
    long_term_memory_str = ""
    metaprompt = "You're my assistant to help me!"
    while True:
        user_input=input("-----Round{}-----\n".format(round))
        print("------user_input------",user_input)
        # short_term_memory=user_input+res

        # print("------The type of short_term_memory_str------",type(short_term_memory_str))
        print("------short_term_memory_str------",short_term_memory_str)
        prompt=metaprompt+long_term_memory_str+short_term_memory_str+user_input
        print("------prompt------", prompt)

        res=openai_reply(prompt)
        short_term_memory.append(user_input+res)
        # print("------short_term_memory------", short_term_memory)
        short_term_memory_str=str(short_term_memory)

        if round%summary_and_forgetting_frequence==0:
            long_term_memory_str = summary(short_term_memory_str)
            short_term_memory_str=""

        print("------long_term_memory_str------",long_term_memory_str)
        print("------res------",res)
        round=round+1

# In test environment,we set it to 2
# In development environment,we set it to 5
memoryrepository_talk(2)