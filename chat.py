import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(
    api_key = os.getenv("ANTHROPIC_API_KEY")
)

message = client.messages.create(
    max_tokens = 1024,
    messages = [
        {
            "role": "user",
            "content": "Hello Claude",
        }
    ],
    model="claude-sonnet-4-5-20250929"
)

print(message.content)
