#!/usr/bin/python3
"""Unittest for max_integer([...])
"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    def test_ordered_max_integer(self):
        """test an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_max_integer(self):
        """test unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_max_list(self):
        """test empty list"""
        self.assertEqual(max_integer([]), None)
    
    def test_1_element_max_list(self):
        self.assertEqual(max_integer([5]), 5)
    
    def test_float_max_list(self):
        self.assertEqual(max_integer([8.0, 9.5, 1]), 9.5)

if __name__ == "__main__":
    unittest.main()