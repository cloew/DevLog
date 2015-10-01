from ..file_structure import FileStructure

class LogYear:
    """ Represents a specific Log Year directory """
    
    def __init__(self, date):
        """ Initialize with the date to wrap """
        self.date = date
        
    @lazy_property
    def path(self):
        """ Return the path to this Year """
        return FileStructure.getYearDirname(self, self.date)