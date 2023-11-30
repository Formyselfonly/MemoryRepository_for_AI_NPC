# Function calling allows you
# to more reliably get structured data back from the model.
import os

from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(
    api_key=OPENAI_API_KEY
)


def get_openai_reply(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system",
             "content": "You're my helpful JSON output assistant,output all response in json format,and give the simple answer for me"},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )
    return response.choices[0].message.content


ans = get_openai_reply("How many basic color in the world?")
print(ans)
