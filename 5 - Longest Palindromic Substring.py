# An O(len(s)^2) solution with O(1) space
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        longestPalindrome = ""
        for i in range(1, len(s)):
            # Consider i as the center of an odd length Palindrome
            low = i-1
            high = i+1
            while low >= 0 and high < len(s) and s[low] == s[high]:
                low -= 1
                high += 1
            if high-(low+1) > len(longestPalindrome):
                longestPalindrome = s[low+1:high]
            # Consider i-1, i as the center of an even length Palindrome
            low = i-1
            high = i
            if s[low] != s[high]:
                continue
            while s[low] == s[high]:
                low -= 1
                high += 1
                if low < 0 or high == len(s):
                    break
            if high-(low+1) > len(longestPalindrome):
                longestPalindrome = s[low+1:high]
        return longestPalindrome