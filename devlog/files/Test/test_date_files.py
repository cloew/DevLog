from ..date_files import DateFiles
import unittest
from unittest.mock import patch, Mock

import datetime

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