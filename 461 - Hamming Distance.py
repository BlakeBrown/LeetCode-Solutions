# Algorithm is pretty straight forward, take the bigger of x, y
# and use that to determine how many bits there are.

# Compare bits and increment everytime they don't match.

# Let's use a generator just for practice.
# https://wiki.python.org/moin/Generators
class Solution(object):
    def createGenerator(self, n):
        ret = 1
        while ret <= n:
            yield ret
            ret *= 2
        yield ret*2
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        big = max(x,y)
        generator = self.createGenerator(big)
        count = 0
        for i in generator:
            if (x & i) != (i & y):
                count += 1
        return count