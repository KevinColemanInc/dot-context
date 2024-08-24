class CodeExecutor:
    def __init__(self) -> None:
        pass
    
    # Persist code from the LLM response and persists to the file path
    def persist_code(llm_response, inst_filepath):
        # Persist the code from the LLM response to the code filepath
        code_filepath = inst_filepath.removesuffix(".instruct")
        with open(code_filepath, "w") as code_file:
            code_file.write(llm_response)