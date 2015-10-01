from .config import Config
from kao_path import TouchDirectory, TouchFile
import os
            
def create_path(createFn):
    """ Decorator to create a path from the path provided """
    def decorator(fn):
        def wrapper(self, date, create=False):
            path = fn(self, date, create=create)
            if create:
                createFn(path)
            return path
        return wrapper
    return decorator
            
create_dir = create_path(TouchDirectory)
create_file = create_path(TouchFile)

class FileStructure:
    """ Helper class to manage the File Structure for the dev log """
    
    def getFilename(self, date, create=False):
        """ Return the filename for the log on the date """
        if create:
            TouchDirectory(Config.logDir)
        return self.getDayFilename(date, create=create)

    @create_dir
    def getYearDirname(self, date, create=False):
        """ Return the path to the year directory """
        return os.path.join(Config.logDir, str(date.year))
        
    @create_dir
    def getMonthDirname(self, date, create=False):
        """ Return the path to the month directory """
        return os.path.join(self.getYearDirname(date, create=create), str(date.month))
        
    @create_file
    def getDayFilename(self, date, create=False):
        """ Return the path to the day file """
        return os.path.join(self.getMonthDirname(date, create=create), str(date.day))
        
FileStructure = FileStructure()