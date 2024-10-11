from openai import OpenAI
import os
import dotenv
from pathlib import Path
dotenv.load_dotenv()
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")
openai=OpenAI(
    api_key=OPENAI_API_KEY
)

def openai_reply(prompt):
    completions=openai.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role":"system","content":"You're my assistant"},
            {"role":"user","content":prompt}
        ]
    )
    return completions.choices[0].message.content
def npc_reply(prompt):
    completions=openai.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role":"system","content":"You're NPC"},
            {"role":"user","content":prompt}
        ]
    )
    return completions.choices[0].message.content

def openai_reply_json(prompt):
    completions=openai.chat.completions.create(
      model="gpt-3.5-turbo-1106",
      response_format={ "type": "json_object" },
      messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": prompt}
      ]
    )
    return completions.choices[0].message.content


def openai_reply_embedding(input):
    completions=openai.embeddings.create(
    input=input,
    model="text-embedding-ada-002"
    )
    return completions.data[0].embedding

def openai_fine_tuning(file_json):
    openai.files.create(
        # file=open("test.jsonl", "rb"),
        file=open(file_json, "rb"),
        purpose="fine-tune"
    )
    openai.fine_tuning.jobs.create(
        training_file="trainingfile-abc123",
        model="gpt-3.5-turbo-1106"
    )

def openai_fine_tuning_using(fine_tuning_model,prompt):
    # model = "fine_tuning_modelft:gpt-3.5-turbo:my-org:custom_suffix:id",
    completions = openai.chat.completions.create(
        model = fine_tuning_model,
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content":prompt}
        ]
    )
    return completions.choices[0].message

def openai_image_reply(prompt):
    completions = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = completions.data[0].url

def openai_vision_reply(prompt):
    completions = openai.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    return completions.choices[0]

def openai_text2speech_reply(input,speech_file_obj_path):
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = openai.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=input
    )
    response.stream_to_file(speech_file_obj_path)


def openai_speech2text_reply(audio_input):
    # audio_file = open("/path/to/file/audio.mp3", "rb")
    audio_file = open(audio_input, "rb")
    transcript = openai.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    return transcript
