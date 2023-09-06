#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class test_max_integer(unittest.TestCase):
    def test_max_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def negative_number(self):

        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([-42]), -42)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
