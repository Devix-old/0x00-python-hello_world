#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
'''This code to test the base class'''


class TestBase(unittest.TestCase):
    '''Represente TestBase class'''

    def test_base_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_base_custom_id(self):
        b2 = Base(100)
        self.assertEqual(b2.id, 100)

    def test_to_json_string_empty_list(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_with_dicts(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_str = Base.to_json_string([dictionary])
        self.assertEqual(
            json_str,
            '[{"id": 2, "_Rectangle__width": 10, "_Rectangle__height": 7, '
            '"_Rectangle__x": 2, "_Rectangle__y": 8}]'
        )


if __name__ == "__main__":
    unittest.main()
