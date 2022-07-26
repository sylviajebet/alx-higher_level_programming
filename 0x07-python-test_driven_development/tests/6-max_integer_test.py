#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [2, 7, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [8, 6, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 8)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [5]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [18.3, 4.09, -11.2, 6.841, 7.001]
        self.assertEqual(max_integer(floats), 4.09)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [18.3, 3, 4.09, -11.2, 21]
        self.assertEqual(max_integer(ints_and_floats), 4.09)

    def test_string(self):
        """Test a string."""
        string = "Sylvia"
        self.assertEqual(max_integer(string), 'v')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Sylvia", "is", "a", "star"]
        self.assertEqual(max_integer(strings), "is")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()