from .config import Config
from .file_structure import FileStructure

from subprocess import call

class Editor:
    """ Represents the Editor to use to open files """
    
    def open(self, dates):
        """ Open the given dates """
        filenames = [FileStructure.getFilename(date, create=True) for date in dates]
        call(Config.editorCommandString.split() + filenames)
        
Editor = Editor()