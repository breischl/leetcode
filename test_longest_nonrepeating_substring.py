import unittest
import longest_nonrepeating_substring


class TestLongestNonrepeatingSubstring(unittest.TestCase):
    def setUp(self):
        self.s = longest_nonrepeating_substring.Solution()

    def test(self):
        self.assertEqual(0, self.s.lengthOfLongestSubstring(""))
        self.assertEqual(1, self.s.lengthOfLongestSubstring("a"))
        self.assertEqual(1, self.s.lengthOfLongestSubstring("aaaaaaa"))
        self.assertEqual(1, self.s.lengthOfLongestSubstring(" "))
        self.assertEqual(2, self.s.lengthOfLongestSubstring("ab"))
        self.assertEqual(3, self.s.lengthOfLongestSubstring("abca"))
        self.assertEqual(3, self.s.lengthOfLongestSubstring("abcc"))
        self.assertEqual(3, self.s.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(4, self.s.lengthOfLongestSubstring("abcazbcbb"))
        self.assertEqual(4, self.s.lengthOfLongestSubstring("abcazbbcaz"))
