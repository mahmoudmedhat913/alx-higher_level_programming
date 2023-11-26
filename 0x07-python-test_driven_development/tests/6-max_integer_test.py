#!/usr /bin /python3
"""Unittest for max integer module"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test case for max integer function"""

    def test_regular(self):
        l = [1, 2, 3, 4, 5]
        result = max_integer(l)
        self.assertEqual(result, 5)

    def test_not_int(self):
        l = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, l)

    def test_empty(self):
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_negative(self):
        l = [-2, -6, -1]
        result = max_integer(l)
        self.assertEqual(result, -1)

    def test_float(self):
        l = [3, 4.5, 2]
        result = max_integer(l)
        self.assertEqual(result, 4.5)

    def test_not_list(self):
        self.assertRaises(TypeError, max_integer, 7)
    
    def test_unique(self):
        l = [45]
        result = max_integer(l)
        self.assertEqual(result, 45)

    def test_identical(self):
        l = [8, 8, 8, 8, 8]
        result = max_integer(l)
        self.assertEqual(result, 8)

    def test_strings(self):
        l = ["hi", "hello"]
        result = max_integer(l)
        self.assertEqual(result, "hi")

    def test_none(self):
        self.assertRaises(TypeError, max_integer, None)


if __name__ == '__main__':
    unittest.main()
