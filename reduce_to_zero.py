'''
For Leetcode problem #1342 https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
'''


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps: int = 0

        while num > 0:
            steps += 1
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1

        return steps