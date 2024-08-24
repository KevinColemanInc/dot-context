from octoai.text_gen import ChatMessage


class PromptConstructor:
    def __init__(self, context_manager):
        self.context_manager = context_manager

    def create_messages(self):
        context_explanation = (
            "The `context` array contains the following files and instructions:\n"
        )
        for item in self.context_manager.get_context():
            context_explanation += item

        files_explanation = self.context_manager.get_inst()

        system_message_content = (
            f"Below are the details about the context and files:\n\n"
            f"{context_explanation}\n"
            f"{files_explanation}\n"
            "Please use this information to understand the structure and purpose of each component."
        )

        user_message_content = "Please proceed with the instructions provided."

        messages = [
            ChatMessage(content=system_message_content.strip(), role="system"),
            ChatMessage(content=user_message_content.strip(), role="user"),
        ]

        return messages
