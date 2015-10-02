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