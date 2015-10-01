from ..log_year import LogYear
import unittest
from unittest.mock import patch, Mock

from datetime import date, timedelta

class previous(unittest.TestCase):
    """ Test cases of previous """
        
    def test_previous(self):
        """ Test that when there is a previous year, it is returned """
        today = date.today()
        otherYear = today - timedelta(days=366)
        year = LogYear(today)
        expected = LogYear(otherYear)
        items = [expected.date.year, year.date.year]
        
        itemsMock = Mock(return_value=items)
        
        with patch('devlog.dates.log_year.GetDirContents', new_callable=Mock(return_value=itemsMock)):
            actual = year.previous
            self.assertEqual(actual, expected)
        
    def test_noPrevious(self):
        """ Test that when there is no previous year, None is returned """
        today = date.today()
        year = LogYear(today)
        expected = None
        items = [year.date.year]
        
        itemsMock = Mock(return_value=items)
        
        with patch('devlog.dates.log_year.GetDirContents', new_callable=Mock(return_value=itemsMock)):
            actual = year.previous
            self.assertEqual(actual, expected)

class next(unittest.TestCase):
    """ Test cases of next """
        
    def test_previous(self):
        """ Test that when there is a next year, it is returned """
        today = date.today()
        otherYear = today - timedelta(days=366)
        year = LogYear(today)
        expected = LogYear(otherYear)
        items = [year.date.year, expected.date.year]
        
        itemsMock = Mock(return_value=items)
        
        with patch('devlog.dates.log_year.GetDirContents', new_callable=Mock(return_value=itemsMock)):
            actual = year.next
            self.assertEqual(actual, expected)
        
    def test_noNext(self):
        """ Test that when there is no next year, None is returned """
        today = date.today()
        year = LogYear(today)
        expected = None
        items = [year.date.year]
        
        itemsMock = Mock(return_value=items)
        
        with patch('devlog.dates.log_year.GetDirContents', new_callable=Mock(return_value=itemsMock)):
            actual = year.next
            self.assertEqual(actual, expected)