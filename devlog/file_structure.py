from .config import Config
import os

class FileStructure:
    """ Helper class to manage the File Structure for the dev log """
    
    def getFilename(self, date):
        """ Return the filename for the log on the date """
        return self.getDayFilename(date)
        
    def getYearDirname(self, date):
        """ Return the path to the year directory """
        return os.path.join(Config.logDir, str(date.year))
        
    def getMonthDirname(self, date):
        """ Return the path to the month directory """
        return os.path.join(self.getYearDirname(date), str(date.month))
        
    def getDayFilename(self, date):
        """ Return the path to the day file """
        return os.path.join(self.getMonthDirname(date), str(date.day))
        
FileStructure = FileStructure()