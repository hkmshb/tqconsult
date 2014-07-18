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



if __name__ == "__main__":
    unittest.main()
