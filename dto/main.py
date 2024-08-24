import sys

from code_generator import CodeGenerator
from code_executor import CodeExecutor
from file_importer import import_files
from prompt_constructor import PromptConstructor


# Main process file
def main(inst_file_path):
    # Step 1: Import files and populate the ContextManager
    context_manager = import_files(inst_file_path)

    # Step 2: Construct the messages for the prompt using the PromptConstructor
    prompt_constructor = PromptConstructor(context_manager)
    messages = prompt_constructor.create_messages()

    # Step 3: Generate the code using the CodeGenerator
    code_generator = CodeGenerator(messages)
    llm_response = code_generator.generate_code()

    # Step 4: Extract the code and persist to disk
    code_executor = CodeExecutor()
    code_executor.extract_code(llm_response, inst_file_path)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_inst_file>")
    else:
        inst_file_path = sys.argv[1]
        main(inst_file_path)
