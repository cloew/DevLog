from kao_try import Try

class LogDay:
    """ Represents a specific Log Day file """
    
    def __init__(self, date, month):
        """ Initialize with the date to wrap and the parent month """
        self.date = date
        self.month = month
        
    @property
    def previous(self):
        """ Return the previous day """
        if self.month.days.first != self:
            return self.month.days.previous(self)
        else:
            return Try(self).month.previous.days.last.done()
        
    @property
    def next(self):
        """ Return the next day """
        if self.month.days.last != self:
            return self.month.days.next(self)
        else:
            return Try(self).month.next.days.first.done()
        
    def __eq__(self, other):
        """ Return if this Day is the same as another """
        return self.date.year == other.date.year and self.date.day == other.date.day and self.month == other.month
        
    def __repr__(self):
        """ Return the String representation of this class """
        return "<LogDay({0})>".format(self.date)