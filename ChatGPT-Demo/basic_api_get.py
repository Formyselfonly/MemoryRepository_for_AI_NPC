#Setup
from openai import OpenAI
import os
import dotenv
dotenv.load_dotenv()
client=OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)
completion=client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {"role":"system","content":"You're My Personal Assistant"},
        {"role":"user","content":"请列举 10 个中国流行的地图导航软件"}
    ]
)
print(completion.choices[0].message)
