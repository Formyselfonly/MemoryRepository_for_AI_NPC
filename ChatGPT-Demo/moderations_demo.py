import os
import dotenv
from openai import OpenAI
import json
dotenv.load_dotenv()
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")
client = OpenAI(
    api_key=OPENAI_API_KEY
)


response = client.moderations.create(input="I really hate u!I want to kill u!")
print(response.results[0])
