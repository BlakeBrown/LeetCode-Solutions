# Solution #1 - Brute Force Recursion
class Solution(object):
    def countSolutions(self, n, count):
        if n == 1:
            return count
        if n % 2 == 0:
            return self.countSolutions(n/2, count+1)
        return min(self.countSolutions(n+1, count+1),self.countSolutions(n-1, count+1))
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.countSolutions(n,0)


# Solution #2 - Smart recursion
# Let's be smarter about what to do when n is odd
# Basically we want to maximize the number of times we can divide by 2.
# If n+1 is divisible by 4 then we will get an extra division by performing n+1.
# The only edge case is 3, since we don't gain anything from the extra division,
# i.e we want to do 3 -> 2 -> 1 instead of 3 -> 4 -> 2 -> 1.
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        # n = 3 is an edge case where adding 1 isn't better
        if n == 3:
            return 2
        if n % 2 == 0:
            return 1 + self.integerReplacement(n/2)
        if (n+1) % 4 == 0:
            return 1 + self.integerReplacement(n+1)
        return 1 + self.integerReplacement(n-1)
        