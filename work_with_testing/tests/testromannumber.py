import unittest

from work_with_testing.mycode import RomanNumberConvert


class RomanNumberConvertTest(unittest.TestCase):
    def setUp(self):
        self.svt = RomanNumberConvert()

    def test_parsing_centry(self):
        self.assertEqual(100, self.svt.convert_to_decimal('C'))

    def test_parsing_six(self):
        self.assertEqual(6, self.svt.convert_to_decimal('VI'))

    def test_empty_roman_number(self):
        self.assertRaises(TypeError, self.svt.convert_to_decimal, None)

    def test_zero_roman_number(self):
        self.assertTrue(self.svt.convert_to_decimal("") == 0)


if __name__ == '__main__':
    unittest.main()
