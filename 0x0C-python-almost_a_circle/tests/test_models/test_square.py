#!/usr/bin/python3
'''Define Test_square module !'''
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    '''Represente the class TestSquare !'''

    def test_size_getter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.id, 1)

    def test_size_setter_valid(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_invalid(self):
        s = Square(5)
        self.assertEqual(str(s), "[Square] (2) 0/0 - 5")
        with self.assertRaises(TypeError) as context:
            s.size = "9"
        self.assertEqual(
            str(context.exception),
            "width must be an integer"
        )

    def test_update_square(self):
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (5) 0/0 - 5")
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        expected_dict = {'id': 4, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dictionary, expected_dict)
        self.assertTrue(isinstance(s1_dictionary, dict))


if __name__ == "__main__":
    unittest.main()
