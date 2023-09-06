#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_int(self):
        """Test when the list has positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        """Test when the list is empty."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test when the list has negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test when the list has both positive and negative integers."""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_single_element_list(self):
        """Test when the list contains only a single element."""
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([-42]), -42)

    def test_duplicate_max(self):
        """Test when the list contains duplicate maximum values."""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_max_in_middle(self):
        """Test when the maximum value is in the middle of the list."""
        self.assertEqual(max_integer([1, 2, 5, 2, 1]), 5)

    def test_max_at_start(self):
        """Test when the maximum value is at the start of the list."""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_at_end(self):
        """Test when the maximum value is at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 99]), 99)
