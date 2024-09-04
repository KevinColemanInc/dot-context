from dotcontext.run.code_generator import CodeGenerator
from dotcontext.run.code_executor import CodeExecutor
from dotcontext.run.file_importer import import_files
from dotcontext.run.prompt_constructor import PromptConstructor


def run(inst_file_path):
    # Step 1: Import files and populate the ContextManager
    context_manager = import_files(inst_file_path)

    # Step 2: Construct the messages for the prompt using the PromptConstructor
    prompt_constructor = PromptConstructor(context_manager)
    messages = prompt_constructor.create_messages()

    # Step 3: Generate the code using the CodeGenerator
    code_generator = CodeGenerator(messages)
    llm_response = code_generator.generate_code()

    # Step 4: Persist the generated code to the disk
    code_executor = CodeExecutor()
    code_executor.persist_code(llm_response, inst_file_path)
