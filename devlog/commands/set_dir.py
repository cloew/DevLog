from ..config import Config
from kao_command.args import Arg

class SetDir:
    """ Command to set the current editor """
    description = "Set the path to the devlog parent directory"
    args = [Arg('path', action='store', help="The Path to the directory where logs will be stored")]
    
    def run(self, *, path):
        """ Set the Log Directory """
        Config.setLogDir(path)