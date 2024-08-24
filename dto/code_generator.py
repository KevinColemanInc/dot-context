import os

from dotenv import load_dotenv
from octoai.client import OctoAI
from octoai.text_gen import ChatMessage

load_dotenv()


class CodeGenerator:
    def __init__(self, messages: list[ChatMessage]) -> None:
        self.messages = messages
        self.client = OctoAI(api_key=os.getenv("OCTOAI_API_KEY"))

    def generate_code(self):
        response = self.client.text_gen.create_chat_completion(
            max_tokens=65536,
            messages=self.messages,
            model="meta-llama-3.1-405b-instruct",
            presence_penalty=0,
            temperature=0,
            top_p=1,
        )

        return response.dict()["choices"][0]["message"]["content"]
