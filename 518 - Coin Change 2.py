class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        change = [0] * (amount+1)
        change[0] = 1 # can always make 0 change
        for c in coins:
            for i in range(c,amount+1):
                change[i] = change[i] + change[i-c]
        return change[amount]