import os
import dotenv
from pathlib import Path
from openai import OpenAI
import json
dotenv.load_dotenv()
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")
client = OpenAI(
    api_key=OPENAI_API_KEY
)


speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)

