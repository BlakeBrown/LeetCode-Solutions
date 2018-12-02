# Solution 1: We can always form N with 1 term
# Try forming N with 2 terms, 3 terms, etc. until no longer possible

class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 1
        k = 2 # number of consecutive terms
        i = int(N/k) # starting number in series
        while self.triangleNumber(k) <= N:
            triangle = self.triangleNumber(k-1)
            total = i*k + triangle
            if (N-total)%k == 0:
              ans += 1
            k += 1
            i = int(N/k)
        return ans
    
# Solution 2: Simplify the logic, we don't actually care about the starting number in the series
class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 1
        k = 2 # number of consecutive terms
        while self.triangleNumber(k) <= N:
            triangle = self.triangleNumber(k-1)
            if (N-triangle)%k == 0:
              ans += 1
            k += 1
        return ans
    
    def triangleNumber(self, n):
        return int(n*(n+1)/2)

# Solution 3: Let's use DP to keep track of triangle instead of repeating calculations
class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 1
        k = 2 # number of consecutive terms
        triangle = 1
        while triangle + k <= N:
            if (N-triangle)%k == 0:
              ans += 1
            triangle += k
            k += 1
        return ans
                