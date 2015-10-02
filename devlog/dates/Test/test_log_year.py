from ..log_month import LogMonth
from ..log_year import LogYear
import unittest
from unittest.mock import patch, Mock

from kao_list import KaoList
from Test import BuildDate

class previous(unittest.TestCase):
    """ Test cases of previous """
        
    def test_previous(self):
        """ Test that when there is a previous year, it is returned """
        firstYear = BuildDate(year=2015)
        secondYear = BuildDate(year=2014)
        year = LogYear(firstYear)
        expected = LogYear(secondYear)
        items = [expected.date, year.date]
        
        itemsMock = Mock(return_value=items)
        
        with patch('devlog.dates.log_year.FileStructure') as FileStructureMock:
            FileStructureMock.years = itemsMock
            actual = year.previous
            self.assertEqual(actual, expected)
        
    def test_noPrevious(self):
        """ Test that when there is no previous year, None is returned """
        yearDate = BuildDate(year=2015)
        year = LogYear(yearDate)
        expected = None
        items = [year.date]
        
        itemsMock = Mock(return_value=items)
        
        with patch('devlog.dates.log_year.FileStructure') as FileStructureMock:
            FileStructureMock.years = itemsMock
            actual = year.previous
            self.assertEqual(actual, expected)

class next(unittest.TestCase):
    """ Test cases of next """
        
    def test_next(self):
        """ Test that when there is a next year, it is returned """
        firstYear = BuildDate(year=2015)
        secondYear = BuildDate(year=2014)
        year = LogYear(firstYear)
        expected = LogYear(secondYear)
        items = [year.date, expected.date]
        
        itemsMock = Mock(return_value=items)
        
        with patch('devlog.dates.log_year.FileStructure') as FileStructureMock:
            FileStructureMock.years = itemsMock
            actual = year.next
            self.assertEqual(actual, expected)
        
    def test_noNext(self):
        """ Test that when there is no next year, None is returned """
        yearDate = BuildDate(year=2015)
        year = LogYear(yearDate)
        expected = None
        items = [year.date]
        
        itemsMock = Mock(return_value=items)
        
        with patch('devlog.dates.log_year.FileStructure') as FileStructureMock:
            FileStructureMock.years = itemsMock
            actual = year.next
            self.assertEqual(actual, expected)

class all(unittest.TestCase):
    """ Test cases of all """
        
    def test_build(self):
        """ Test that the years are built properly and return """
        dates = [BuildDate(year=year) for year in [2012, 2013, 2014]]
        year = LogYear(dates[0])
        expected = KaoList([LogYear(date) for date in dates])
        
        itemsMock = Mock(return_value=dates)
        
        with patch('devlog.dates.log_year.FileStructure') as FileStructureMock:
            FileStructureMock.years = itemsMock
            actual = year.all
            FileStructureMock.years.assert_called_once_with()
            self.assertEqual(actual, expected)

class months(unittest.TestCase):
    """ Test cases of months """
        
    def test_build(self):
        """ Test that the months are built properly and return """
        dates = [BuildDate(month=month) for month in [8, 9, 10]]
        year = LogYear(dates[0])
        expected = KaoList([LogMonth(date, year) for date in dates])
        
        itemsMock = Mock(return_value=dates)
        
        with patch('devlog.dates.log_year.FileStructure') as FileStructureMock:
            FileStructureMock.months = itemsMock
            actual = year.months
            FileStructureMock.months.assert_called_once_with(year.date)
            self.assertEqual(actual, expected)