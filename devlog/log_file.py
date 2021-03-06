from .dates import LogDay, LogMonth, LogYear
from .files import DateFiles
from kao_decorators import lazy_property

class LogFile:
    """ Represents a log file """
    
    def __init__(self, date, create=False):
        """ Initialize with the date """
        self.date = date
        self.create = create
        
    @lazy_property
    def path(self):
        """ Return the path to this log file """
        return DateFiles.Days.path(self.date, create=self.create)
    
    @property
    def previous(self):
        """ Return the previous LogFile """
        previous = self.day.previous
        return LogFile(previous.date) if previous else None
    
    @property
    def next(self):
        """ Return the next LogFile """
        next = self.day.next
        return LogFile(next.date) if next else None
        
    @property
    def day(self):
        """ Return the LogDay """
        path = self.path # Force file creation if needed
        year = LogYear(self.date)
        month = LogMonth(self.date, year)
        return LogDay(self.date, month)
        