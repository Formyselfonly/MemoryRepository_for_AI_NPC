# Once a model has been fine-tuned,
# you won't need to provide as many examples in the prompt.

from openai import OpenAI
import os
import dotenv
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")
client = OpenAI(
  api_key=OPENAI_API_KEY
)

client.files.create(
  file=open("fine_tuning_data.jsonl", "rb"),
  purpose="fine-tune"
)

client.fine_tuning.jobs.create(
  training_file="fine_tuning_data.jsonl",
  model="gpt-3.5-turbo-1106"
)