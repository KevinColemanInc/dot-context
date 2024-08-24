from langchain_core.prompts import PromptTemplate


class PromptConstructor:
    def __init__(self, context_manager):
        self.context_manager = context_manager

    def create_prompt(self):
        context_explanation = (
            "The `context` array contains the following files and instructions:\n"
        )
        for item in self.context_manager.context:
            context_explanation += f"- Filename: {item['filename']}, Instructions: {item['instructions']}\n"

        files_explanation = (
            "The `files` array contains the following files and instructions:\n"
        )
        for item in self.context_manager.files:
            files_explanation += f"- Filename: {item['filename']}, Instructions: {item['instructions']}\n"

        prompt_text = (
            f"Below are the details about the context and files:\n\n"
            f"{context_explanation}\n"
            f"{files_explanation}\n"
            "Please use this information to understand the structure and purpose of each component."
        )

        prompt_template = PromptTemplate(
            template=prompt_text, input_variables=[], template_format="f-string"
        )
        return prompt_template
