from .contents_helper import GetDirContents
from .date_builder import DateBuilder
from .log_month import LogMonth
from ..file_structure import FileStructure

from kao_decorators import lazy_property, proxy_for
from kao_list import KaoList
from datetime import date
import os

class LogYear:
    """ Represents a specific Log Year directory """
    
    def __init__(self, date):
        """ Initialize with the date to wrap """
        self.date = date
        self.dateBuilder = DateBuilder(date)
        
    @lazy_property
    def path(self):
        """ Return the path to this Year """
        return FileStructure.getYearDirname(self.date)
        
    @lazy_property
    def logDir(self):
        """ Return the path to this Year """
        return os.path.join(self.path, '..')
        
    @property
    def previous(self):
        """ Return the LogYear previous to this one """
        return self.all.previous(self)
        
    @property
    def next(self):
        """ Return the LogYear next to this one """
        return self.all.next(self)
        
    @property
    def all(self):
        """ Return all the years """
        return KaoList([LogYear(self.buildDate(year=year)) for year in GetDirContents(self.logDir)])
        
    @property
    def months(self):
        """ Return all the months within this year """
        return KaoList([LogMonth(self.buildDate(month=month) for month in GetDirContents(self.path))])
        
    @property
    def buildDate(self):
        """ Return the new date """
        return self.dateBuilder.build
        
    def __eq__(self, other):
        """ Return if this Year is the same as another """
        return self.date.year == other.date.year