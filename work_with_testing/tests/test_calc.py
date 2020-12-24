import unittest
from work_with_testing.calc import *


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-10, 4), -6)

    def test_subtraction(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-10, 4), -14)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-10, 4), -40)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-10, 2), -5)
        self.assertRaises(ValueError, divide, 10, 0)

        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()