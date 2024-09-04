import os
import string

from dotcontext.run.context_manager import ContextManager


def import_files(InstFilePath: string) -> ContextManager:
    """Given filepath for .inst file, return contextmanager
    which contains the .inst and all relevant .context files"""
    contextmanager = ContextManager()

    # put .instruct contents into contextmanager
    abspathinst = os.path.abspath(InstFilePath)
    inst = expand_imports(abspathinst)
    contextmanager.set_inst(inst)

    dirpath = os.path.dirname(abspathinst)

    # walk up the directory tree to find .context files
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            if name.endswith(".context"):
                # put .context contents into contextmanager
                currentfile = os.path.abspath(name)
                context = expand_imports(currentfile)
                contextmanager.add_context(context)
    return contextmanager


def expand_imports(FilePath: string) -> string:
    expandedfile = ""
    file = open(FilePath, "r")
    lines = file.readlines()
    for line in lines:
        if line.startswith("@import"):
            importfilepath = line.split()[1]  # get the filepath
            importfile = open(importfilepath, "r")
            expandedfile += importfile.read()
            importfile.close()
        else:
            expandedfile += line
    file.close()
    return expandedfile


# test code
# contextmanager = import_files("instructfile")
# for context in contextmanager.get_context():
#     print(context)
# print(contextmanager.get_inst())
