#!/usr/bin/python3
'''define the module test_rectangle'''
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''Represente the class TestRectangle'''

    def test_valid_attributes(self):
        # Test instantiation with valid attributes
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertEqual(r.id, 50)

    def test_invalid_width(self):
        # Test raising TypeError for invalid width
        with self.assertRaises(TypeError) as context:
            r = Rectangle("invalid", 20)
        self.assertEqual(
            str(context.exception),
            "width must be an integer"
        )

    def test_invalid_height(self):
        # Test raising TypeError for invalid height
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, "invalid")
        self.assertEqual(
            str(context.exception),
            "height must be an integer"
        )

    def test_width_less_than_zero(self):
        # Test raising ValueError for width less than zero
        with self.assertRaises(ValueError) as context:
            r = Rectangle(-10, 20)
        self.assertEqual(
            str(context.exception),
            "width must be > 0"
        )

    def test_height_less_than_zero(self):
        # Test raising ValueError for height less than zero
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, -20)
        self.assertEqual(
            str(context.exception),
            "height must be > 0"
        )

    def test_x_less_than_zero(self):
        # Test raising ValueError for x less than zero
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 20, -30)
        self.assertEqual(
            str(context.exception),
            "x must be >= 0"
        )

    def test_y_less_than_zero(self):
        # Test raising ValueError for y less than zero
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 20, 30, -40)
        self.assertEqual(
            str(context.exception),
            "y must be >= 0"
        )

    def test_rectange_area(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def display_rectangle(self):

        r1 = Rectangle(4, 6)
        r1.display()

        print("---")

        r1 = Rectangle(2, 2)
        r1.display()

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        r1_excpected_ouput = "[Rectangle] (12) 2/1 - 4/6"
        r2_excpected_ouput = "[Rectangle] (8) 1/0 - 5/5"
        self.assertEqual(str(r1), r1_excpected_ouput)
        self.assertEqual(str(r2), r2_excpected_ouput)

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (10) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_with_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

        r.update(width=1, x=2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 2)

        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.id, 89)

        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.width, 4)

    def test_update_with_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(5, 5, 5, 5, 5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        expected_dict = {'_Rectangle__height': 2,
                         '_Rectangle__width': 10,
                         '_Rectangle__x': 1,
                         '_Rectangle__y': 9,
                         'id': 9}
        self.assertEqual(r1_dictionary, expected_dict)
        self.assertTrue(isinstance(r1_dictionary, dict))


if __name__ == "__main__":
    unittest.main()
