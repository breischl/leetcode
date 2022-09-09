class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        for start_idx in range(0, len(s)):
            if max_length >= len(s) - start_idx:
                # If our longest substring is already longer than the remaining letters in the string, we know there aren't any longer ones available
                break

            letters_seen = set()
            length = 0
            for letter in s[start_idx:]:
                if letter in letters_seen:
                    break
                else:
                    letters_seen.add(letter)
                    length += 1

            max_length = max(length, max_length)

        return max_length
