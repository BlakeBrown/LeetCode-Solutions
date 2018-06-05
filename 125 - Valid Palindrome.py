class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s2 = ""
        for c in s:
            if c.isalnum():
                s2 += c
        
        s2 = s2.lower()
        for i in range(len(s2)/2):
            if s2[i] != s2[len(s2)-i-1]:
                return False
        return True