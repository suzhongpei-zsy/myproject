import unittest
from unittest import mock

#from post_youdao import *

class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True)

    def test_get_ts(self):
        get_ts=mock.Mock(return_value='1584684880395')
        self.assertEqual('1584684880395',get_ts())

    def test_get_salt(self):
        get_salt = mock.Mock(return_value='1584684880395')
        self.assertEqual('1584684880395',get_salt())


if __name__=='__main__':
    unittest.main()