#Why and when use embedding?
# Embeddings are numerical representations
# of concepts converted to number sequences,
# which make it easy for computers to understand
# the relationships between those concepts.
# Since the initial launch of the OpenAI /embeddings endpoint,
# many applications have incorporated embeddings to personalize,
# recommend, and search content.

from openai import OpenAI
import os
import dotenv
dotenv.load_dotenv()
apikey=os.environ.get("OPENAI_API_KEY")
client=OpenAI(
    api_key=apikey
)

response=client.embeddings.create(
    input="What are u doing?",
    model="text-embedding-ada-002"
)

print(response.data[0].embedding)