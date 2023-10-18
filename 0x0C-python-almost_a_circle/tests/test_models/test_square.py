#!/usr/bin/python3
'''Define Test_square module !'''
import unittest
from models.square import Square
import os


class TestSquare(unittest.TestCase):
    '''Represente the class TestSquare !'''

    def test_size_getter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.id, 13cccccccccccccccccccccccccccccccccccccc)

    def test_size_setter_valid(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_invalid(self):
        s = Square(5)
        self.assertEqual(str(s), "[Square] (14) 0/0 - 5")
        with self.assertRaises(TypeError) as context:
            s.size = "9"
        self.assertEqual(
            str(context.exception),
            "width must be an integer"
        )

    def test_update_square(self):
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (18) 0/0 - 5")
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
        expected_dict = {'id': 17, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s1_dictionary, expected_dict)
        self.assertTrue(isinstance(s1_dictionary, dict))

    def test_valid_square_creation(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

    def test_square_with_x_and_y(self):
        s2 = Square(2, 2)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.width, 2)
        self.assertEqual(s2.height, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)  # Default value for y

    def test_square_with_x_y_and_id(self):
        s3 = Square(3, 1, 3, 42)
        self.assertEqual(s3.size, 3)
        self.assertEqual(s3.width, 3)
        self.assertEqual(s3.height, 3)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.id, 42)

    def test_create_square_with_id(self):
        square_data = {'id': 89}
        s = Square.create(**square_data)
        self.assertEqual(s.id, 89)

    def test_create_square_with_id_and_size(self):
        square_data = {'id': 89, 'size': 1}
        s = Square.create(**square_data)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

    def test_create_square_with_id_size_x_and_y(self):
        square_data = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s = Square.create(**square_data)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)


if __name__ == "__main__":
    unittest.main()
