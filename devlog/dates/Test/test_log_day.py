from ..log_day import LogDay
from ..log_month import LogMonth
import unittest
from unittest.mock import Mock

from Test import BuildDate

class previous(unittest.TestCase):
    """ Test cases of previous """
        
    def test_notFirstOfMonth(self):
        """ Test that when the day is not the first of the month, the previous is found properly """
        current = BuildDate(day=10)
        otherDay = BuildDate(day=9)
        month = Mock()
        
        day = LogDay(current, month)
        expected = LogMonth(otherDay, month)
        
        month.days.first.__ne__ = Mock(return_value=True)
        month.days.previous = Mock(return_value=expected)
        
        actual = day.previous
        month.days.first.__ne__.assert_called_once_with(day)
        month.days.previous.assert_called_once_with(day)
        self.assertEqual(expected, actual)
        
    def test_firstOfMonth(self):
        """ Test that when the day is the first of the month, the previous is found properly """
        current = BuildDate(day=10)
        month = Mock()
        
        day = LogDay(current, month)
        expected = Mock()
        
        month.days.first.__ne__ = Mock(return_value=False)
        month.previous.days.last = expected
        
        actual = day.previous
        month.days.first.__ne__.assert_called_once_with(day)
        self.assertFalse(month.months.previous.called)
        self.assertEqual(expected, actual)

class next(unittest.TestCase):
    """ Test cases of next """
        
    def test_notLastOfMonth(self):
        """ Test that when the day is not the last of the month, the next is found properly """
        current = BuildDate(day=10)
        otherDay = BuildDate(day=9)
        month = Mock()
        
        day = LogDay(current, month)
        expected = LogMonth(otherDay, month)
        
        month.days.last.__ne__ = Mock(return_value=True)
        month.days.next = Mock(return_value=expected)
        
        actual = day.next
        month.days.last.__ne__.assert_called_once_with(day)
        month.days.next.assert_called_once_with(day)
        self.assertEqual(expected, actual)
        
    def test_lastOfMonth(self):
        """ Test that when the day is the last of the month, the next is found properly """
        current = BuildDate(day=10)
        month = Mock()
        
        day = LogDay(current, month)
        expected = Mock()
        
        month.days.last.__ne__ = Mock(return_value=False)
        month.next.days.first = expected
        
        actual = day.next
        month.days.last.__ne__.assert_called_once_with(day)
        self.assertFalse(month.months.next.called)
        self.assertEqual(expected, actual)