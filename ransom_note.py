class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        all_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        magazine_letters = {i: 0 for i in all_letters}

        for l in magazine:
            magazine_letters[l] = magazine_letters[l] + 1

        for l in ransomNote:
            count = magazine_letters[l]
            if count == 0:
                return False
            else:
                magazine_letters[l] = count - 1

        return True
