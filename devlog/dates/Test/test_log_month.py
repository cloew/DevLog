from ..log_day import LogDay
from ..log_month import LogMonth
from ..log_year import LogYear
import unittest
from unittest.mock import patch, Mock

from kao_list import KaoList
from Test import BuildDate

class previous(unittest.TestCase):
    """ Test cases of previous """
        
    def test_notFirstOfYear(self):
        """ Test that when the month is not the first of the year, the previous is found properly """
        current = BuildDate(month=10)
        otherMonth = BuildDate(month=9)
        year = Mock()
        
        month = LogMonth(current, year)
        expected = LogMonth(otherMonth, year)
        
        year.months.first.__ne__ = Mock(return_value=True)
        year.months.previous = Mock(return_value=expected)
        
        actual = month.previous
        year.months.first.__ne__.assert_called_once_with(month)
        year.months.previous.assert_called_once_with(month)
        self.assertEqual(expected, actual)
        
    def test_firstOfYear(self):
        """ Test that when the month is the first of the year, the previous is found properly """
        current = BuildDate(month=10)
        year = Mock()
        
        month = LogMonth(current, year)
        expected = Mock()
        
        year.months.first.__ne__ = Mock(return_value=False)
        year.previous.months.last = expected
        
        actual = month.previous
        year.months.first.__ne__.assert_called_once_with(month)
        self.assertFalse(year.months.previous.called)
        self.assertEqual(expected, actual)

class next(unittest.TestCase):
    """ Test cases of next """
        
    def test_notLastOfYear(self):
        """ Test that when the month is not the last of the year, the next is found properly """
        current = BuildDate(month=10)
        otherMonth = BuildDate(month=9)
        year = Mock()
        
        month = LogMonth(current, year)
        expected = LogMonth(otherMonth, year)
        
        year.months.last.__ne__ = Mock(return_value=True)
        year.months.next = Mock(return_value=expected)
        
        actual = month.next
        year.months.last.__ne__.assert_called_once_with(month)
        year.months.next.assert_called_once_with(month)
        self.assertEqual(expected, actual)
        
    def test_lastOfYear(self):
        """ Test that when the month is the last of the year, the next is found properly """
        current = BuildDate(month=10)
        year = Mock()
        
        month = LogMonth(current, year)
        expected = Mock()
        
        year.months.last.__ne__ = Mock(return_value=False)
        year.next.months.first = expected
        
        actual = month.next
        year.months.last.__ne__.assert_called_once_with(month)
        self.assertFalse(year.months.next.called)
        self.assertEqual(expected, actual)

class days(unittest.TestCase):
    """ Test cases of days """
        
    def test_build(self):
        """ Test that the days are built properly and return """
        dates = [BuildDate(day=day) for day in [8, 9, 10]]
        year = LogYear(dates[0])
        month = LogMonth(dates[0], year)
        expected = KaoList([LogDay(date, month) for date in dates])
        
        itemsMock = Mock(return_value=dates)
        
        with patch('devlog.dates.log_month.DateFiles') as DateFilesMock:
            DateFilesMock.Days = itemsMock
            actual = month.days
            DateFilesMock.Days.assert_called_once_with(month.date)
            self.assertEqual(actual, expected)