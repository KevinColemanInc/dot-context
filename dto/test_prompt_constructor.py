from octoai.text_gen import ChatMessage
from prompt_constructor import PromptConstructor


def test_prompt_constructor():
    class MockContextManager:
        def __init__(self):
            self.context = [
                {
                    "filename": "test/path/to/context1",
                    "instructions": "These are instructions for context1.",
                },
                {
                    "filename": "test/path/to/context2",
                    "instructions": "These are instructions for context2.",
                },
            ]
            self.files = [
                {
                    "filename": "test/path/to/file1",
                    "instructions": "These are instructions for file1.",
                },
                {
                    "filename": "test/path/to/file2",
                    "instructions": "These are instructions for file2.",
                },
            ]

    mock_context_manager = MockContextManager()
    prompt_constructor = PromptConstructor(mock_context_manager)

    messages = prompt_constructor.create_messages()

    expected_messages = [
        ChatMessage(
            content=(
                "Below are the details about the context and files:\n\n"
                "The `context` array contains the following files and instructions:\n"
                "- Filename: test/path/to/context1, Instructions: These are instructions for context1.\n"
                "- Filename: test/path/to/context2, Instructions: These are instructions for context2.\n\n"
                "The `files` array contains the following files and instructions:\n"
                "- Filename: test/path/to/file1, Instructions: These are instructions for file1.\n"
                "- Filename: test/path/to/file2, Instructions: These are instructions for file2.\n\n"
                "Please use this information to understand the structure and purpose of each component."
            ),
            role="system",
        ),
        ChatMessage(
            content="Please proceed with the instructions provided.", role="user"
        ),
    ]

    if messages != expected_messages:
        print(
            "Test case failed! The generated messages do not match the expected output."
        )
        print("\n--- Expected Messages ---\n")
        print(expected_messages)
        print("\n--- Generated Messages ---\n")
        print(messages)
    else:
        print("Test case passed!")


if __name__ == "__main__":
    test_prompt_constructor()
