from datetime import date

class DateBuilder:
    """ Helper class to construct a date """
    
    def __init__(self, date):
        """ Initialize with the date to start with """
        self.date = date
        
    def build(self, year=None, month=None, day=None):
        """ Build a new date overriding values from the original with those provided """
        year = year if year is not None else self.date.year
        month = month if month is not None else self.date.month
        day = day if day is not None else self.date.day
        return date(year, month, day)