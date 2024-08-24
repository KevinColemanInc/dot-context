import os
import string

from dto.context_manager import ContextManager

def import_files(InstFilePath:string) -> ContextManager:
    """Given filepath for .inst file, return contextmanager
     which contains the .inst and all relevant .context files"""
    contextmanager = ContextManager()
    
    # put inst filename and contents into contextmanager
    abspathinst =  os.path.abspath(InstFilePath)
    file = open(abspathinst,'r')
    instfilecontents = file.read()
    inst = instfilecontents
    contextmanager.set_inst(inst)
    
    dirpath = os.path.dirname(abspathinst)

    # walk up the directory tree to find .context files
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            if name.endswith('.context'):
                # put const filename and contents into contextmanager
                currentfile = os.path.abspath(name)
                file = open(currentfile,'r')
                filecontents = file.read()
                context = filecontents
                contextmanager.add_context(context)
    return contextmanager


# test code
# contextmanager = import_files("instfile")
# for context in contextmanager.get_context():
#     print(context)
# for instruct in contextmanager.get_inst():
#     print(instruct)