from kao_config import GlobalConfigFile
from kao_decorators import lazy_property

import toml

class Config:
    """ Represents the DevLog Configuration """
    CONFIG_FILENAME = ".devlog"
    EDITOR_KEY = 'editor'
    
    @lazy_property
    def config(self):
        """ Return the Config object """
        return GlobalConfigFile(self.CONFIG_FILENAME, create=True)
        
    @property
    def editorCommandString(self):
        """ Return the configured editor command String """
        return self._toml[self.EDITOR_KEY]
        
    def setEditor(self, editorCmd):
        """ Set the editor command """
        self._write(editor=editorCmd.strip())
        
    @property
    def _toml(self):
        """ Return the toml dictionary from the file """
        return toml.loads(self.config.read())
        
    def _write(self, **kwargs):
        """ Write the configuration with the data given """
        self.config.write(toml.dumps(kwargs))
        
Config = Config()