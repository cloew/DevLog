from .config import Config

from subprocess import call

class Editor:
    """ Represents the Editor to use to open files """
    
    def open(self, log):
        """ Open the given log """
        self.openAll([log])
    
    def openAll(self, logs):
        """ Open all the given logs """
        filenames = [log.path for log in logs]
        call(Config.editorCommandString.split() + filenames)
        
Editor = Editor()