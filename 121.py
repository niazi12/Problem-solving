# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = float('inf')
        for price in prices:
            min_buy=min(min_buy, price)
            max_profit=max(max_profit, price-min_buy)
        return max_profit