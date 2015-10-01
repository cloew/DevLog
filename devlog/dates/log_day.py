from ..file_structure import FileStructure

class LogDay:
    """ Represents a specific Log Day file """
    
    def __init__(self, date):
        """ Initialize with the date to wrap """
        self.date = date
        
    @lazy_property
    def path(self):
        """ Return the path to this Day """
        return FileStructure.getFilename(self, self.date)