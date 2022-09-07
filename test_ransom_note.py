import unittest
import ransom_note


class TestRansomNote(unittest.TestCase):
    def setUp(self):
        self.s = ransom_note.Solution()

    def test_basic(self):

        self.assertFalse(self.s.canConstruct("az", "ab"))
        self.assertFalse(self.s.canConstruct("a", "b"))
        self.assertFalse(self.s.canConstruct("a", ""))
        self.assertTrue(self.s.canConstruct("a", "ba"))
        self.assertTrue(self.s.canConstruct("a", "aaaaaa"))
        self.assertTrue(self.s.canConstruct("a", "bbbbabbbb"))

        self.assertTrue(self.s.canConstruct("abbac", "asdfbacccccccbbbbdf"))
