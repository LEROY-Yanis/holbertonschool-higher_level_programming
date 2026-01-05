#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Test with ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with max at beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test with empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Test with one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_floats(self):
        """Test with floats"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_mixed_int_float(self):
        """Test with mixed int and float"""
        self.assertEqual(max_integer([1, 2.5, 3, 2]), 3)

    def test_string_list(self):
        """Test with list of strings"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_none_argument(self):
        """Test with None as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
