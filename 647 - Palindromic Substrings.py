class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i in range(len(s)):
            count = 0
            # Consider s[i] the middle of an odd length palindrome
            low = i
            high = i
            while low >= 0 and high < len(s) and s[low] == s[high]:
                count += 1
                high += 1
                low -= 1
            # Consider s[i] the middle of an even length palindrome
            high = i
            low = i-1
            while low >= 0 and high < len(s) and s[low] == s[high]:
                count += 1
                high += 1
                low -= 1
            total += count
        return total