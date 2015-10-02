from ..config import Config
from .date_fields import DateFields
from kao_path import TouchDirectory, TouchFile
import os
            
def create_path(createFn):
    """ Decorator to create a path from the path provided """
    def decorator(fn):
        def wrapper(self, *args, create=False):
            path = fn(self, *args, create=create)
            if create:
                createFn(path)
            return path
        return wrapper
    return decorator
            
create_dir = create_path(TouchDirectory)
create_file = create_path(TouchFile)

class PathBuilder:
    """ Helper class to manage the build paths for the dev log """
    
    def __init__(self, rootDir):
        """ Initialize with the root directory """
        self.rootDir = rootDir
        self.builders = {DateFields.year: self.getYearDirname,
                         DateFields.month: self.getMonthDirname,
                         DateFields.day: self.getDayFilename}
    
    def getPath(self, date, dateField, create=False):
        """ Return the filename for the log on the date """
        return self.builders[dateField](date, create=create)

    @create_dir
    def getRootDir(self, create=False):
        """ Return the path to the root directory """
        return return Config.logDir

    @create_dir
    def getYearDirname(self, date, create=False):
        """ Return the path to the year directory """
        return os.path.join(self.getRootDir(create=create), str(date.year))
        
    @create_dir
    def getMonthDirname(self, date, create=False):
        """ Return the path to the month directory """
        return os.path.join(self.getYearDirname(date, create=create), str(date.month))
        
    @create_file
    def getDayFilename(self, date, create=False):
        """ Return the path to the day file """
        return os.path.join(self.getMonthDirname(date, create=create), str(date.day))