from kao_config import GlobalConfigFile
from kao_decorators import lazy_property

class Config:
    """ Represents the DevLog Configuration """
    CONFIG_FILENAME = ".devlog"
    
    @lazy_property
    def config(self):
        """ Return the Config object """
        return GlobalConfigFile(self.CONFIG_FILENAME, create=True)
        
    @property
    def editorCommandString(self):
        """ Return the configured editor command String """
        return self.config.readlines()[0].strip()