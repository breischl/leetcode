import unittest
import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.s = fizz_buzz.Solution()

    def test_things(self):
        self.assertEqual(
            ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"], self.s.fizzBuzz(15))
