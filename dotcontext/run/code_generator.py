import os
from octoai.text_gen import ChatMessage


class CodeGenerator:
    def __init__(self, messages: list[ChatMessage]) -> None:
        self.messages = messages
        self.modelName = os.getenv("MODEL")
        if not (os.getenv("OCTOAI_API_KEY") is None):
            from octoai.client import OctoAI

            self.octoAI = OctoAI(api_key=os.getenv("OCTOAI_API_KEY"))
        elif os.getenv("AZURE_OPENAI_ENDPOINT"):
            from langchain_openai import AzureChatOpenAI

            model = AzureChatOpenAI(
                azure_deployment="gpt-35-turbo",
                api_version="2023-06-01-preview"
            )
            self.azureChat = model

    def generate_code(self):
        if hasattr(self, 'octoAI'):
            response = self.octoAI.text_gen.create_chat_completion(
                max_tokens=65536,
                messages=self.messages,
                model=self.modelName,
                presence_penalty=0,
                temperature=0,
                top_p=1,
            )

            return response.dict()["choices"][0]["message"]["content"]
        else:
            from langchain_core.messages import HumanMessage, SystemMessage

            langChainMessages = [
                HumanMessage(content=self.messages[0].content),
                SystemMessage(content=self.messages[1].content),
            ]
            response = self.azureChat.invoke(langChainMessages)
            print("\n\n" + langChainMessages[0].content + "\n---\n")
            print("\n\n" + langChainMessages[1].content + "\n---\n")
            print("\n\n" + response.content+ "\n")

            return response.content
