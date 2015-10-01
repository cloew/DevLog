from .file_structure import FileStructure
from kao_decorators import lazy_property

class LogFile:
    """ Represents a log file """
    
    def __init__(self, date, create=False):
        """ Initialize with the date """
        self.date = date
        self.create = create
        
    @lazy_property
    def path(self):
        """ Return the path to this log file """
        return FileStructure.getFilename(self.date, create=self.create)