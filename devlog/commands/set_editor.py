from ..config import Config
from kao_command.args import Arg

class SetEditor:
    """ Command to set the current editor """
    description = "Set the editor command"
    args = [Arg('cmd', action='store', help="The Command String to use to open the log editor")]
    
    def run(self, *, cmd):
        """ Run with the specified cmd string """
        Config.setEditor(cmd)