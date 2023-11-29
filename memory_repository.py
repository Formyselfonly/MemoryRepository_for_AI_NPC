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



def summarize_content_prompt(content, user_name, boot_name, language='en'):
    prompt = '请总结以下的对话内容，尽可能精炼，提取对话的主题和关键信息。如果有多个关键事件，可以分点总结。对话内容：\n' if language == 'cn' else 'Please summarize the following dialogue as concisely as possible, extracting the main themes and key information. If there are multiple key events, you may summarize them separately. Dialogue content:\n'
    for dialog in content:
        query = dialog['query']
        response = dialog['response']
        # prompt += f"\n用户：{query.strip()}"
        # prompt += f"\nAI：{response.strip()}"
        prompt += f"\n{user_name}：{query.strip()}"
        prompt += f"\n{boot_name}：{response.strip()}"
    prompt += ('\n总结：' if language == 'cn' else '\nSummarization：')
    return prompt


def summarize_overall_prompt(content, language='en'):
    prompt = '请高度概括以下的事件，尽可能精炼，概括并保留其中核心的关键信息。概括事件：\n' if language == 'cn' else "Please provide a highly concise summary of the following event, capturing the essential key information as succinctly as possible. Summarize the event:\n"
    for date, summary_dict in content:
        summary = summary_dict['content']
        prompt += (
            f"\n时间{date}发生的事件为{summary.strip()}" if language == 'cn' else f"At {date}, the events are {summary.strip()}")
    prompt += ('\n总结：' if language == 'cn' else '\nSummarization：')
    return prompt


def summarize_overall_personality(content, language='en'):
    prompt = '以下是用户在多段对话中展现出来的人格特质和心情，以及当下合适的回复策略：\n' if language == 'cn' else "The following are the user's exhibited personality traits and emotions throughout multiple dialogues, along with appropriate response strategies for the current situation:"
    for date, summary in content:
        prompt += (
            f"\n在时间{date}的分析为{summary.strip()}" if language == 'cn' else f"At {date}, the analysis shows {summary.strip()}")
    prompt += (
        '\n请总体概括用户的性格和AI恋人最合适的回复策略，尽量简洁精炼，高度概括。总结为：' if language == 'cn' else "Please provide a highly concise and general summary of the user's personality and the most appropriate response strategy for the AI lover, summarized as:")
    return prompt


def summarize_person_prompt(content, user_name, boot_name, language):
    prompt = f'请根据以下的对话推测总结{user_name}的性格特点和心情，并根据你的推测制定回复策略。对话内容：\n' if language == 'cn' else f"Based on the following dialogue, please summarize {user_name}'s personality traits and emotions, and devise response strategies based on your speculation. Dialogue content:\n"
    for dialog in content:
        query = dialog['query']
        response = dialog['response']
        # prompt += f"\n用户：{query.strip()}"
        # prompt += f"\nAI：{response.strip()}"
        prompt += f"\n{user_name}：{query.strip()}"
        prompt += f"\n{boot_name}：{response.strip()}"

    prompt += (
        f'\n{user_name}的性格特点、心情、{boot_name}的回复策略为：' if language == 'cn' else f"\n{user_name}'s personality traits, emotions, and {boot_name}'s response strategy are:")
    return prompt

