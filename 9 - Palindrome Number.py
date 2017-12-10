# O(n) space and O(n) time: Convert the integer to a string and check if it's a palindrome.
# Why is this bad? Uses an additional O(n) space where n is the number of digits in the integer.
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xString = str(x)
        for i, c in enumerate(xString):
            if i > (len(xString)/2):
                break
            if(xString[i] != xString[len(xString)-i-1]):
                return False
        return True

# TODO: Better algorithm uses O(logn) space & time by only using integers, not strings.
# Note that an integer takes up O(logn) space where n is the number of digits.