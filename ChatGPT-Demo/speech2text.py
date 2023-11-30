from openai import OpenAI
import os
import dotenv
from pathlib import Path
from openai import OpenAI
import json
dotenv.load_dotenv()
client = OpenAI()

audio_file= open("/path/to/file/audio.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)