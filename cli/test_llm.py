import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY environment variable not set")

from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)
completion = client.chat.completions.create(
  model="openrouter/free",
  messages = [
    {
        "role": "user",
        "content": "Why is Boot.dev such a great place to learn about RAG? Use one paragraph maximum."   }
]
)

print(completion.choices[0].message.content)
print(f"Prompt tokens: {completion.usage.prompt_tokens}")
print(f"Response tokens: {completion.usage.completion_tokens}")
