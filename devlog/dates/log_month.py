from .log_day import LogDay
from ..files import DateFiles

from kao_list import KaoList
from kao_try import Try

class LogMonth:
    """ Represents a specific Log Month directory """
    
    def __init__(self, date, year):
        """ Initialize with the date to wrap and the parent year """
        self.date = date
        self.year = year
        
    @property
    def previous(self):
        """ Return the previous month """
        if self.year.months.first != self:
            return self.year.months.previous(self)
        else:
            return Try(self).year.previous.months.last.done()
        
    @property
    def next(self):
        """ Return the next month """
        if self.year.months.last != self:
            return self.year.months.next(self)
        else:
            return Try(self).year.next.months.first.done()
        
    @property
    def days(self):
        """ Return all the days within this month """
        return KaoList([LogDay(date, self) for date in DateFiles.Days(self.date)])
        
    def __eq__(self, other):
        """ Return if this Month is the same as another """
        return self.year == other.year and self.date.month == other.date.month
        
    def __repr__(self):
        """ Return the String representation of this class """
        return "<LogMonth({0})>".format(self.date)