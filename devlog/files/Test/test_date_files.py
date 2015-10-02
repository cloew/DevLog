from ..date_files import DateFiles
import unittest
from unittest.mock import patch, Mock

import datetime

class DateFileMock:
    def __init__(self, field, results=[], contents=[], path=None):
        self.field = field
        self.build = Mock(side_effect=results)
        self.path = Mock(return_value=path)
        self.getDirContents = Mock(return_value=contents)

class call(unittest.TestCase):
    """ Test cases of call """
        
    def test_entriesBuilt(self):
        """ Test that entries are built properly """
        date = datetime.date(year=2015, month=1, day=1)
        items = range(10)
        path = "Some/Path"
        expected = ["Something - " + str(i) for i in range(len(items))]
        dateFiles = DateFileMock('not year', results=expected, contents=items, path=path)
        
        actual = DateFiles.__call__(dateFiles, date)
        
        dateFiles.path.assert_called_once_with(date)
        dateFiles.getDirContents.assert_called_once_with(path)
        for item in items:
            dateFiles.build.assert_any_call(date, item)
        self.assertEqual(actual, expected)
        
        
    @patch('devlog.files.date_files.datetime')
    def test_noDateProvided_Year(self, DatetimeMock):
        """ Test that when no date is provided, but the Date Type is Year, the entries are built properly """
        dateToUse = datetime.date(year=2015, month=1, day=1)
        items = range(10)
        path = "Some/Path"
        expected = ["Something - " + str(i) for i in range(len(items))]
        dateFiles = DateFileMock('year', results=expected, contents=items, path=path)
        
        DatetimeMock.date.today = Mock(return_value=dateToUse)
        
        try:
            actual = DateFiles.__call__(dateFiles)
            
            dateFiles.path.assert_called_once_with(dateToUse)
            dateFiles.getDirContents.assert_called_once_with(path)
            for item in items:
                dateFiles.build.assert_any_call(dateToUse, item)
            self.assertEqual(actual, expected)
        except TypeError:
            self.fail('A TypeError should not be thrown for the date argument when the Date Type is year')
        
    def test_noDateProvided_NotYear(self):
        """ Test that when no date is provided, but the Date Type is not Year, the call throws an Exception """
        dateFiles = DateFileMock('not year')
        
        self.assertRaises(TypeError, DateFiles.__call__, dateFiles)

class build(unittest.TestCase):
    """ Test cases of build """
        
    def test_built(self):
        """ Test that the date is built properly """
        date = datetime.date(year=2015, month=1, day=1)
        newValue = 3
        dateFiles = DateFiles.Days
        expected = "Something"
        
        builderInstance = Mock()
        builderInstance.build = Mock(return_value=expected)
        
        with patch('devlog.files.date_files.DateBuilder', return_value=builderInstance) as DateBuilderMock:
            actual = dateFiles.build(date, newValue)
            DateBuilderMock.assert_called_once_with(date)
            builderInstance.build.assert_called_once_with(**{dateFiles.field: newValue})
            self.assertEqual(actual, expected)

class path(unittest.TestCase):
    """ Test cases of path """
        
    def test_path(self):
        """ Test that the date is built properly """
        date = datetime.date(year=2015, month=1, day=1)
        createFlag = "Gibberish..."
        dateFiles = DateFiles.Days
        expected = "Something"
        
        builderInstance = Mock()
        builderInstance.getPath = Mock(return_value=expected)
        
        with patch('devlog.files.date_files.PathBuilder', return_value=builderInstance) as PathBuilderMock:
            actual = dateFiles.path(date, create=createFlag)
            PathBuilderMock.assert_called_once_with()
            builderInstance.getPath.assert_called_once_with(date, dateFiles.field, create=createFlag)
            self.assertEqual(actual, expected)