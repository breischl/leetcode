'''
For Leetcode #1672 Richest Customer Wealth https://leetcode.com/problems/richest-customer-wealth/
'''


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(map(sum, accounts))
