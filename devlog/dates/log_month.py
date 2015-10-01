from ..file_structure import FileStructure
from kao_decorators import lazy_property

class LogMonth:
    """ Represents a specific Log Month directory """
    
    def __init__(self, date, year):
        """ Initialize with the date to wrap and the parent year """
        self.date = date
        self.year = year
        
    @lazy_property
    def path(self):
        """ Return the path to this Month """
        return FileStructure.getMonthDirname(self, self.date)
        
    @property
    def previous(self):
        """ Return the previous month """
        if self.neighbors.first != self:#!self.isFirst:
            return self.neighbors.previous(self)
        else:
            return self.year.previous.months.last