class Solution:
    '''
        Converts Roman numerals to base-10 integer value for LeetCode problem #13
    '''

    digits_map: dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        digits_arr: list[int] = [self.digits_map[l] for l in list(s)]
        total: int = 0
        prev_digit: int = 0

        for digit_value in reversed(digits_arr):
            if digit_value < prev_digit:
                total -= digit_value
            else:
                total += digit_value
            prev_digit = digit_value

        return total
