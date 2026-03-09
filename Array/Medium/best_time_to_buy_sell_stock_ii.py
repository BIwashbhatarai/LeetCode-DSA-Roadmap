"""
File: best_time_to_buy_sell_stock_ii.py
Problem: Best Time to Buy and Sell Stock II
Description: Given an array of stock prices, calculate the maximum profit
by buying and selling multiple times.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        profit = 0

        # Loop through prices and add all upward differences
        for i in range(n - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]

        return profit


if __name__ == "__main__":
    # Example usage
    obj = Solution()
    print(obj.maxProfit([7, 6, 4, 3, 1]))  # Output: 0
    print(obj.maxProfit([1, 2, 3, 4, 5]))  # Output: 4
