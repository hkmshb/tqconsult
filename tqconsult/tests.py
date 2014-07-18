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
    
    
    @unpack
    @data(["How now, Mrs. Brown Cow", " ", ["How","now,","Mrs.","Brown","Cow"]],
          ["How now, Mrs. Brown Cow", ",", ["How now", " Mrs. Brown Cow"]],
          ["How now, Mrs. Brown Cow", ".", ["How now, Mrs", " Brown Cow"]])
    def test_tokenize_string(self, input_string, delimiter, expected):
        result = solutions.tokenize_string(input_string, delimiter)
        self.assertListEqual(result, expected)
    
    
    @unpack
    @data(["How now, Mrs. Brown Cow", [".", ","], ["How now"," Mrs"," Brown Cow"]],
          ["How now, Mrs. Brown Cow", [" ", ".", ","], ["How","now","Mrs","Brown","Cow"]])
    def test_tokenize_string2(self, input_string, delimiter, expected):
        result = solutions.tokenize_string2(input_string, delimiter)
        self.assertListEqual(result, expected)
    
    
    @unpack
    @data([[1,2,3,4,5,6],  0, [1,2,3,4,5,6]],
          [[1,2,3,4,5,6],  1, [6,1,2,3,4,5]],
          [[1,2,3,4,5,6],  2, [5,6,1,2,3,4]],
          [[1,2,3,4,5,6],  3, [4,5,6,1,2,3]],
          [[1,2,3,4,5,6],  4, [3,4,5,6,1,2]],
          [[1,2,3,4,5,6],  5, [2,3,4,5,6,1]],
          [[1,2,3,4,5,6],  6, [1,2,3,4,5,6]],
          [[1,2,3,4,5,6], -2, [5,6,1,2,3,4]],)
    def test_rotate(self, array, npos, expected):
        result = solutions.rotate(array, npos)
        self.assertListEqual(result, expected)
    
    
    @unpack
    @data([[1,2,3], 6], 
          [[4,5], 20],
          [[4,6,8], 24])
    def test_lcm(self, array, lcm):
        result = solutions.lcm(array)
        self.assertEqual(result, lcm)
    
    
    
if __name__ == "__main__":
    unittest.main()
    
    
