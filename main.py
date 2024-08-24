# Example usage
manager = ContextManager()
manager.add_context("First context string")
manager.add_context("Second context string")
print(
    manager.get_context()
)  # Output: ['First context string', 'Second context string']
manager.remove_context("First context string")
print(manager.get_context())  # Output: ['Second context string']

# main.py
# Sharon
context_manager = import_files(ARGS[0])  # in: file path; out: context_manager

#
prompt = build_prompt(context_manager)  # out: langchain prompt

# this writes to disk
# michael
execute_prompt(prompt)  # in: langchain prompt # out: None
