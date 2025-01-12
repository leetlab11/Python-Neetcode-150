# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
  
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 
# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SLIDING WINDOW:
# Two pointers move in the same direction
# one variable will be selling price(r) and one will be buying(l)
# only move selling price iteratively
# moving buying price only when minimum is found
# Start at 0 and 1 index
# maintain a profit variable to calculate max profit, initiating at 0
# compare l and r -> if l < r, calculate profit and update the profit variable to get max profit, move r one place further
# if l > r, profits are negative, so move l. Now, l can move 1 step, but there's no point in doing that
# currently, r is at the minimum point and we want l to be at minimum
# so we move l to r's place
# increment r in any case
# continue loop until r is out of bounds


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
            
        return profit

Time Complexity: O(n)
Space Complexity: O(1)

# Companies:
# Amazon- 34
# Google- 21
# Meta- 17
# Microsoft- 11
# Morgan Stanley- 6
# Tiktok- 3
# Salesforce- 3
# Tech Mahindra- 2
# Adobe- 2
# Zoho- 8
# Apple- 5
# Uber- 5
# Nvidia- 4
# Accenture- 4
# Infosys- 3
# Samsung- 3
# Paypal- 3
# TCS- 2
# Oracle- 2
# Yahoo- 26
# Goldman Sachs- 25
# Yandex- 22
# IBM- 17
# JP Morgan- 15
# Bolt- 12
# Walmart Labs- 11
# Zoox- 9
# Media.net- 8
# Citadel- 6
