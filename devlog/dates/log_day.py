from ..file_structure import FileStructure
from kao_decorators import lazy_property

class LogDay:
    """ Represents a specific Log Day file """
    
    def __init__(self, date, month):
        """ Initialize with the date to wrap and the parent month """
        self.date = date
        self.month = month
        
    @lazy_property
    def path(self):
        """ Return the path to this Day """
        return FileStructure.getFilename(self, self.date)
        
    @property
    def previous(self):
        """ Return the previous day """
        if self.neighbors.first != self:#!self.isFirst:
            return self.neighbors.previous(self)
        else:
            return self.month.previous.days.last