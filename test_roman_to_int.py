import unittest
import roman_to_int


class TestRomanToInt(unittest.TestCase):
    def setUp(self):
        self.r = roman_to_int.Solution()

    def test_single_digits(self):
        self.assertEqual(1, self.r.romanToInt("I"))
        self.assertEqual(5, self.r.romanToInt("V"))
        self.assertEqual(10, self.r.romanToInt("X"))
        self.assertEqual(50, self.r.romanToInt("L"))
        self.assertEqual(100, self.r.romanToInt("C"))
        self.assertEqual(500, self.r.romanToInt("D"))
        self.assertEqual(1000, self.r.romanToInt("M"))

    def test_double_digits(self):
        self.assertEqual(2, self.r.romanToInt("II"))

        self.assertEqual(6, self.r.romanToInt("VI"))
        self.assertEqual(4, self.r.romanToInt("IV"))

        self.assertEqual(20, self.r.romanToInt("XX"))
        self.assertEqual(9, self.r.romanToInt("IX"))
        self.assertEqual(11, self.r.romanToInt("XI"))
        self.assertEqual(15, self.r.romanToInt("XV"))

        self.assertEqual(60, self.r.romanToInt("LX"))
        self.assertEqual(40, self.r.romanToInt("XL"))

        self.assertEqual(200, self.r.romanToInt("CC"))
        self.assertEqual(90, self.r.romanToInt("XC"))
        self.assertEqual(110, self.r.romanToInt("CX"))

        self.assertEqual(400, self.r.romanToInt("CD"))
        self.assertEqual(600, self.r.romanToInt("DC"))

        self.assertEqual(2000, self.r.romanToInt("MM"))
        self.assertEqual(900, self.r.romanToInt("CM"))
        self.assertEqual(1100, self.r.romanToInt("MC"))

    def test_complex(self):
        self.assertEqual(3, self.r.romanToInt("III"))
        self.assertEqual(58, self.r.romanToInt("LVIII"))
        self.assertEqual(1994, self.r.romanToInt("MCMXCIV"))
