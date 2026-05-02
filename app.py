import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Create client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Send request
response = client.responses.create(
    model="gpt-4o-mini",  # safe model to start
    input="Introduce yourself."
)

print(response.output_text)