from ..editor import Editor
from ..log_file import LogFile
from kao_command.args import Arg
from datetime import datetime

class NewLog:
    """ Command to create a new log entry """
    description = "Create a new log entry for today"
    args = []
    
    def run(self):
        """ Create the new log entry """
        log = LogFile(datetime.now(), create=True)
        previous = log.previous
        logs = [previous] if previous else []
        logs.append(log)
        Editor.openAll(logs)