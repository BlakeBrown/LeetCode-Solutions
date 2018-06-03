# Solution 1: Solve this problem using recursion.
# If we have a letter or . with no * after, we must match
# Otherwise if we have a * after, we try every number of characters
# Runtime is exponential: O(len(s)^len(p))
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Base case: Nothing left to match
        if len(p) == 0:
            return len(s) == 0
        # If the first letter in p is a star, we should ignore it (no character to repeat)
        if p[0] == "*":
            return self.isMatch(s,p[1:])
        # If we get to this point, p[0] is either a character or a .
        # Case 1: No star after
        if len(p) == 1 or p[1] != "*":
            if len(s) == 0:
                return False
            if p[0] == ".":
                return self.isMatch(s[1:],p[1:])
            if p[0] != s[0]:
                return False
            return self.isMatch(s[1:],p[1:])
        # Case 2: Star after
        # Repeat char zero times
        if self.isMatch(s,p[2:]):
            return True
        # Repeat as many times as we match the input string
        index = 0
        while(index < len(s) and (s[index] == p[0] or p[0] == ".")):
            if self.isMatch(s[index+1:],p[2:]):
                return True
            index += 1
        return False

# Solution 2: We can use dynamic programming to speed up our solution.
# Memoize previous solutions so we aren't resolving the same <s,p> 
# The runtime for this solution is O(len(s)*len(p)) which is tricky to see
# due to the recursion, but we can imagine a worst case scenario.
# Ex. s = "aaaaaaaab", p = "a*a*a*a*" in which case the string doesn't match
# but for every a* we need to expand it len(s) times

class Solution(object):
    lookup = {}
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if (s,p) in self.lookup:
            return self.lookup[(s,p)]
        # Base case: Nothing left to match
        if len(p) == 0:
            self.lookup[(s,p)] = (len(s) == 0)
            return self.lookup[(s,p)]
        # If the first letter in p is a star, we should ignore it (no character to repeat)
        if p[0] == "*":
            self.lookup[(s,p)] = self.isMatch(s,p[1:])
            return self.lookup[(s,p)]
        # If we get to this point, p[0] is either a character or a .
        # Case 1: No star after
        if len(p) == 1 or p[1] != "*":
            if len(s) == 0:
                self.lookup[(s,p)] = False
                return False
            if p[0] == ".":
                self.lookup[(s,p)] = self.isMatch(s[1:],p[1:])
                return self.lookup[(s,p)]
            if p[0] != s[0]:
                self.lookup[(s,p)] = False
                return False
            self.lookup[(s,p)] = self.isMatch(s[1:],p[1:])
            return self.lookup[(s,p)]
        # Case 2: Star after
        # Repeat char zero times
        if self.isMatch(s,p[2:]):
            self.lookup[(s,p)] = True
            return True
        # Repeat as many times as we match the input string
        index = 0
        while(index < len(s) and (s[index] == p[0] or p[0] == ".")):
            self.lookup[(s,p)] = self.isMatch(s[index+1:],p[2:])
            if self.lookup[(s,p)]:
                return True
            index += 1
        self.lookup[(s,p)] = False
        return False
