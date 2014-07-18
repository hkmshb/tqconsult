"""
Transquisite Consulting Pre-Test Questions from eHealth Systems Africa.
Unit tests for codes in tqcon_resp.py 
"""

import unittest
from ddt import ddt, data, unpack

import solutions


@ddt
class Test(unittest.TestCase):
    
    @unpack
    @data(["abcdef", "ebook cd", "bcde"],
          ["fedcba", "ebook cd", "edcb"],
          ["blank cheque", "bank queue", "bank eque"])
    def test_find_chars(self, string1, string2, expected):
        result = solutions.find_chars(string1, string2)
        self.assertTrue(result==expected)
    
    
    @unpack
    @data(["abcdef", "ebook cd", "bcde"],
          ["fedcba", "ebook cd", "edcb"],
          ["blank cheque", "bank queue", "bank eque"])
    def test_find_chars2(self, string1, string2, expected):
        result = solutions.find_chars2(string1, string2)
        self.assertTrue(result==expected)
    
    
    @unpack
    @data([[1,3,7,7,8,9,9,10], 6, [1,3,7,8,9,10]],
          [[1,5,5,8,9,9,9,11,11], 5, [1,5,8,9,11]])
    def test_compact(self, array, count, expected):
        result = solutions.compact(array)
        self.assertEqual(count, result)
        self.assertListEqual(array, expected)


if __name__ == "__main__":
    unittest.main()
