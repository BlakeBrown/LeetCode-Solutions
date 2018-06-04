# Solution 1: Using dynamic programming. This solution takes O(n) time and O(n) space.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0 # no transaction can be made
        right = [0] * len(prices)
        right[len(prices)-1] = prices[len(prices)-1]
        for i in range(len(prices)-2,-1,-1):
            if prices[i] > right[i+1]:
                right[i] = prices[i]
            else:
                right[i] = right[i+1]
        ans = 0
        for i in range(len(prices)):
            if right[i] - prices[i] > ans:
                ans = right[i] - prices[i]
        return ans

# Solution 2: We can do better. Here's a solution in O(n) time and O(1) space.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0 # no transaction can be made
        minPrice = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            if prices[i] - minPrice > ans:
                ans = prices[i] - minPrice
        return ans