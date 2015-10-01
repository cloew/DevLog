from ..file_structure import FileStructure

class LogMonth:
    """ Represents a specific Log Month directory """
    
    def __init__(self, date):
        """ Initialize with the date to wrap """
        self.date = date
        
    @lazy_property
    def path(self):
        """ Return the path to this Month """
        return FileStructure.getMonthDirname(self, self.date)