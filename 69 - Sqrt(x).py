# Solution 1: Brute force
# Runtime: O(sqrt(n))
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        sqrt = 1
        while sqrt*sqrt <= x:
            sqrt += 1
        return sqrt-1

# Solution 2: Use Newton's iterative method to repeatively "guess" sqrt(n)
# Say we want sqrt(4)
# Guess: 4
# Improve our guess to (4+(4/4)) / 2 = 2.5
# Guess: 2.5
# Improve our guess to (2.5+(4/2.5)) / 2 = 2.05
# ...
# We get to 2 very quickly

# Runtime: O(logn)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Use newton's iterative method
        delta = 0.0001
        guess = x
        while guess**2 - x > delta:
            guess = (guess+(x/guess))/2.0
        return int(guess)