from queue import Empty
import unittest
import palindrome_linked_list


class TestPalindromeLinkedList(unittest.TestCase):
    def setUp(self):
        self.s = palindrome_linked_list.Solution()

    def test_single(self):
        self.assertTrue(self._test_palindrome([1]))
        self.assertTrue(self._test_palindrome([0]))

    def test_double(self):
        self.assertTrue(self._test_palindrome([1, 1]))
        self.assertTrue(self._test_palindrome([2, 2]))
        self.assertFalse(self._test_palindrome([2, 1]))
        self.assertFalse(self._test_palindrome([2, 3]))

    def test_1221(self):
        self.assertTrue(self._test_palindrome([1, 2, 2, 1]))

    def test_1220(self):
        self.assertFalse(self._test_palindrome([1, 2, 2, 0]))

    def test_12321(self):
        self.assertTrue(self._test_palindrome([1, 2, 3, 2, 1]))

    def test_1221221(self):
        self.assertTrue(self._test_palindrome([1, 2, 2, 3, 2, 2, 1]))

    def _test_palindrome(self, arr: list[int]) -> None:
        linker = self._link(arr)
        return self.s.isPalindrome(linker)

    def _link(self, arr: list[int]) -> palindrome_linked_list.ListNode:
        if len(arr):
            return palindrome_linked_list.ListNode(arr[0], self._link(arr[1:]))
        else:
            return None
