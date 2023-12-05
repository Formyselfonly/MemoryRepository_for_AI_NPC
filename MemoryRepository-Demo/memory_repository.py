from gpt_utils import openai_reply
def summary(short_term_memory):
    summary=openai_reply("The first is the user's dialogue with the AI, the second is the AI's dialogue with the user. By analogy, odd numbers correspond to users, and even numbers correspond to AI.Summarize the following conversation simply, clearly, and clearly,and mark the speaker:`{}`. And Summary this in no more than two setence.".format(short_term_memory))
    return summary
# short_memory=[]
# long_memory=[]
# meta_prompt="You're Dio Brando:https://jojowiki.com/Dio_Brando"
# memory=short_memory+long_memory
# def generate_prompt(talk):
#     return meta_prompt+memory+talk

# MemoryBank里面有中英结合版本的
# 我为了重构是纯英文版本的

def summarize_content_prompt(content, user_name, boot_name, language='en'):
    prompt = 'Please summarize the following dialogue as concisely as possible, extracting the main themes and key information. If there are multiple key events, you may summarize them separately. Dialogue content:\n'
    for dialog in content:
        query = dialog['query']
        response = dialog['response']
        # prompt += f"\nAI：{response.strip()}"
        prompt += f"\n{user_name}：{query.strip()}"
        prompt += f"\n{boot_name}：{response.strip()}"
    prompt += ('\n总结：' if language == 'cn' else '\nSummarization：')
    return prompt


def summarize_overall_prompt(content, language='en'):
    prompt = "Please provide a highly concise summary of the following event, capturing the essential key information as succinctly as possible. Summarize the event:\n"
    for date, summary_dict in content:
        summary = summary_dict['content']
        prompt += (
            f"At {date}, the events are {summary.strip()}")
    prompt += ('\nSummarization：')
    return prompt


def summarize_overall_personality(content, language='en'):
    prompt = "The following are the user's exhibited personality traits and emotions throughout multiple dialogues, along with appropriate response strategies for the current situation:"
    for date, summary in content:
        prompt += (
            f"At {date}, the analysis shows {summary.strip()}")
    prompt += (
        "Please provide a highly concise and general summary of the user's personality and the most appropriate response strategy for the AI lover, summarized as:")
    return prompt


def summarize_person_prompt(content, user_name, boot_name, language):
    prompt = f"Based on the following dialogue, please summarize {user_name}'s personality traits and emotions, and devise response strategies based on your speculation. Dialogue content:\n"
    for dialog in content:
        query = dialog['query']
        response = dialog['response']
        # prompt += f"\nAI：{response.strip()}"
        prompt += f"\n{user_name}：{query.strip()}"
        prompt += f"\n{boot_name}：{response.strip()}"

    prompt += (
        f"\n{user_name}'s personality traits, emotions, and {boot_name}'s response strategy are:")
    return prompt

