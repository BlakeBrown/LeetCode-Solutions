# Solution 1: Check every needle of the haystack for the needle.
# Runtime: O(len(haystack)*O(len(needle)))

# This TLE's?? I'm not sure why.
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        for i in range(0,len(haystack)):
            found = True
            for j in range(0, len(needle)):
                if i+j >= len(haystack) or haystack[i+j] != needle[j]:
                    found = False
                    break
            if found:
                return i
        return -1

# Solution 2: Let's use slicing in Python and only iterate up to len(haystack)-len(needle)+1
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        for i in range(0,len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1