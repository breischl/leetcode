import unittest
import richest_customer


class TestRichestCustomer(unittest.TestCase):
    def setUp(self):
        self.s = richest_customer.Solution()

    def test(self):
        self.assertEqual(6, self.s.maximumWealth(
            [[1, 2, 3], [3, 2, 1]]
        ))

        self.assertEqual(10, self.s.maximumWealth(
            [[1, 5], [7, 3], [3, 5]]
        ))
