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

    prompt_template = prompt_constructor.create_prompt()

    expected_prompt = (
        "Below are the details about the context and files:\n\n"
        "The `context` array contains the following files and instructions:\n"
        "- Filename: test/path/to/context1, Instructions: These are instructions for context1.\n"
        "- Filename: test/path/to/context2, Instructions: These are instructions for context2.\n\n"
        "The `files` array contains the following files and instructions:\n"
        "- Filename: test/path/to/file1, Instructions: These are instructions for file1.\n"
        "- Filename: test/path/to/file2, Instructions: These are instructions for file2.\n\n"
        "Please use this information to understand the structure and purpose of each component."
    )

    if prompt_template.template != expected_prompt:
        print(
            "Test case failed! The generated prompt does not match the expected output."
        )
        print("\n--- Expected Prompt ---\n")
        print(expected_prompt)
        print("\n--- Generated Prompt ---\n")
        print(prompt_template.template)

        from difflib import unified_diff

        diff = unified_diff(
            expected_prompt.splitlines(keepends=True),
            prompt_template.template.splitlines(keepends=True),
            fromfile="expected",
            tofile="generated",
        )
        print("\n".join(diff))
    else:
        print("Test case passed")


if __name__ == "__main__":
    test_prompt_constructor()
