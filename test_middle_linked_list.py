import unittest
import middle_linked_list
from middle_linked_list import ListNode


class TestMiddleLinkedList(unittest.TestCase):
    def setUp(self):
        self.s = middle_linked_list.Solution()

    def link(self, arr: list[int]) -> ListNode:
        if len(arr):
            return ListNode(arr[0], self.link(arr[1:]))
        else:
            return None

    def test_empty(self):
        self.assertIsNone(self.s.middleNode(None))

    def test_1(self):
        self.assertEqual(1, self.s.middleNode(self.link([1])).val)

    def test_2(self):
        self.assertEqual(2, self.s.middleNode(self.link([1, 2])).val)

    def test_3(self):
        self.assertEqual(2, self.s.middleNode(self.link([1, 2, 3])).val)

    def test_4(self):
        self.assertEqual(3, self.s.middleNode(self.link([1, 2, 3, 4])).val)

    def test_5(self):
        self.assertEqual(3, self.s.middleNode(self.link([1, 2, 3, 4, 5])).val)

    def test_6(self):
        self.assertEqual(4, self.s.middleNode(
            self.link([1, 2, 3, 4, 5, 6])).val)

    def test_7(self):
        self.assertEqual(4, self.s.middleNode(
            self.link([1, 2, 3, 4, 5, 6, 7])).val)

    def test_8(self):
        self.assertEqual(5, self.s.middleNode(
            self.link([1, 2, 3, 4, 5, 6, 7, 8])).val)
