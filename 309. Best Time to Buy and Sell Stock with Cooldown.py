# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
#
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

# Input: [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        # Use 3 dp list to indicate the max profits of every state
        # Hold: hold stock, rest and sold(require hold)
        # Hold : max(hold[i-1], rest[i-1] - price[i])
        # Rest : max(rest[i-1], sold[i-1])
        # Sold : hold[i-1] + price[i]

        n = len(prices)
        # Init 3 dp list

        hold = float("-inf")
        rest = 0
        sold = float("-inf")

        for i in range(n):
            pre_sold = sold
            sold = rest + prices[i]
            hold = max(hold, rest - prices[i])
            rest = max(rest, pre_sold)

        return max(rest, sold)






