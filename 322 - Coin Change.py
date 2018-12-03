import math
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        change = [math.inf] * (amount+1)
        change[0] = 0 # we need zero coins to make zero change
        for coin in coins:
            for i in range(coin, amount+1):
                change[i] = min(change[i], change[i-coin]+1)
        if change[-1] == math.inf:
            return -1
        return change[-1]