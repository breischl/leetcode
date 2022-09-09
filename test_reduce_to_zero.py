import unittest
import reduce_to_zero


class TestReduceToZero(unittest.TestCase):
    def setUp(self):
        self.s = reduce_to_zero.Solution()

    def test_basic(self):
        self.assertEqual(0, self.s.numberOfSteps(0))
        self.assertEqual(1, self.s.numberOfSteps(1))
        self.assertEqual(2, self.s.numberOfSteps(2))
        self.assertEqual(3, self.s.numberOfSteps(3))
        self.assertEqual(3, self.s.numberOfSteps(4))
        self.assertEqual(3, self.s.numberOfSteps(4))
        self.assertEqual(4, self.s.numberOfSteps(8))
        self.assertEqual(6, self.s.numberOfSteps(14))
        self.assertEqual(12, self.s.numberOfSteps(123))
        
