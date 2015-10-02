from .log_month import LogMonth
from ..files import FileStructure

from kao_list import KaoList

class LogYear:
    """ Represents a specific Log Year directory """
    
    def __init__(self, date):
        """ Initialize with the date to wrap """
        self.date = date
        
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
        return KaoList([LogYear(date) for date in FileStructure.years()])
        
    @property
    def months(self):
        """ Return all the months within this year """
        return KaoList([LogMonth(date, self) for date in FileStructure.months(self.date)])
        
    def __eq__(self, other):
        """ Return if this Year is the same as another """
        return self.date.year == other.date.year
        
    def __repr__(self):
        """ Return the String representation of this class """
        return "<LogYear({0})>".format(self.date)