from .date_builder import DateBuilder
from .path_builder import PathBuilder
from ..config import Config

from kao_decorators import proxy_for
import os

@proxy_for('pathBuilder', ['getPath', 'rootDir'])
class FileStructure:
    """ Helper class to manage interacting with the File Structure """
    
    def __init__(self):
        """ Initialize the File Structure """
        self.pathBuilder = PathBuilder(Config.logDir)
        
    def years(self, date):
        """ Return the years """
        builder = DateBuilder(date)
        return [builder.build(year=year) for year in self.getDirContents(self.rootDir)]
        
    def months(self, date):
        """ Return the months """
        builder = DateBuilder(date)
        path = self.pathBuilder.getYearDirname(date)
        return [builder.build(month=month) for month in self.getDirContents(path)]
        
    def days(self, date):
        """ Return the days """
        builder = DateBuilder(date)
        path = self.pathBuilder.getMonthDirname(date)
        return [builder.build(day=day) for day in self.getDirContents(path)]

    def getDirContents(directory):
        """ Return the contents of the given directory """
        return sorted([int(file) for file in os.listdir(directory)])
        
FileStructure = FileStructure()