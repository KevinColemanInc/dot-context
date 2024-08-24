import os
import string

from context_manager import ContextManager

def import_files(InstFilePath:string) -> ContextManager:
    """Given filepath for .inst file, return contextmanager
     which contains the .inst and all relevant .context files"""
    contextmanager = ContextManager()
    abspath =  os.path.abspath(InstFilePath)
    dirpath = os.path.dirname(abspath)

    # walk up the directory tree
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            if name.endswith('.context'):
                currentfile = os.path.abspath(name)
                context = '\'' + currentfile + '\': '
                file = open(currentfile,'r')
                filecontents = file.read()
                context += filecontents
                contextmanager.add_context(context)
    return contextmanager