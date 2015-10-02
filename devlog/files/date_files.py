from .date_fields import DateFields
from .path_builder import PathBuilder
from ..config import Config

import datetime
from enum import Enum

class DateFiles(Enum):
    """ Represents the various kinds of Date Files """
    Years = DateFields.year
    Months = DateFields.month
    Days = DateFields.day
    
    def __call__(self, date=None):
        if date is None:
            if self.value is DateFields.year:
                date = datetime.date.today()
            else:
                raise TypeError('Missing 1 required argument: date')
        return [self.build(date, dateValue) for dateValue in self.getDirContents(self.path(date))]
        
    def path(self, date, create=False):
        return PathBuilder().getPath(date, self.value, create=False)
        
    def build(self, date, value):
        return DateBuilder(self.date).build({self.field, value})

    def getDirContents(self, directory):
        """ Return the contents of the given directory """
        return sorted([int(file) for file in os.listdir(directory)])