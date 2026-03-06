class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(profit, max_profit)

        return max_profit


if __name__ == "__main__":
    obj = Solution()
    print(obj.maxProfit([7, 6, 4, 3, 1]))  # Output: 0
    print(obj.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
