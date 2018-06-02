# O(logn) solution, basic idea is to use recursive exponentiation
# ex. 2^17 = (((2^2)^2)^2)^2 * 2
# ex. 3^6 = (3^2)^2 * 3^2
# ... etc

import math
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n *= -1
        remainder = 1
        original = x
        for i in range(0, int(math.log(n, 2))):
            x *= x
            remainder *= 2
            if x < 0.000000001:
                return 0
        return x * self.myPow(original, n-remainder)