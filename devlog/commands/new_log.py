from ..editor import Editor
from kao_command.args import Arg
from datetime import datetime

class NewLog:
    """ Command to create a new log entry """
    description = "Create a new log entry for today"
    args = []
    
    def run(self):
        """ Create the new log entry """
        Editor.open([datetime.now()])