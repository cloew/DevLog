from .contents_helper import GetDirContents
from .log_month import LogMonth
from ..file_structure import FileStructure

import os

class LogYear:
    """ Represents a specific Log Year directory """
    
    def __init__(self, date):
        """ Initialize with the date to wrap """
        self.date = date
        
    @lazy_property
    def path(self):
        """ Return the path to this Year """
        return FileStructure.getYearDirname(self, self.date)
        
    @property
    def all(self):
        """ Return all the years """
        return [LogYear(year) for year in GetDirContents(os.path.join(self.path, '..'))]
        
    @property
    def months(self):
        """ Return all the months within this year """
        return [LogMonth(month) for month in GetDirContents(self.path)]