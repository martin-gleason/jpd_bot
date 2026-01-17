import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(
    api_key = os.getenv("ANTHROPIC_API_KEY")
)

cli_input = input("|> ")

stream = client.messages.create(
    max_tokens = 1024,
    messages = [
        {
            "role": "user",
            "content": cli_input,
        }
    ],
    model="claude-sonnet-4-5-20250929",
    stream = True
)
