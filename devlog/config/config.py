from kao_config import GlobalConfigFile
from kao_decorators import lazy_property

import os
import toml

EDITOR_KEY = 'editor'
LOG_DIR_KEY = 'log_dir'

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
        return self._toml[EDITOR_KEY]
        
    @property
    def logDir(self):
        """ Return the configured Log Directory """
        return os.path.relpath(self._toml[LOG_DIR_KEY])
        
    def setEditor(self, editorCmd):
        """ Set the editor command """
        tomlConfig = self._toml
        tomlConfig[EDITOR_KEY] = editorCmd.strip()
        self._write(**tomlConfig)
        
    def setLogDir(self, dir):
        """ Set the editor command """
        tomlConfig = self._toml
        tomlConfig[LOG_DIR_KEY] = os.path.abspath(dir.strip())
        self._write(**tomlConfig)
        
    @property
    def _toml(self):
        """ Return the toml dictionary from the file """
        return toml.loads(self.config.read())
        
    def _write(self, **kwargs):
        """ Write the configuration with the data given """
        self.config.write(toml.dumps(kwargs))
        
Config = Config()