# Solution 1: Let's start with a brute force approach.
# If the string is valid, then we only have solution = the string itself
# If the string is not valid, try removing any of the brackets in the string to see if 
# it'll make the string valid. If any one of these work, then we only need to remove one bracket
# and we can just output all valid strings with one bracket removed. 
# Otherwise try removing 2 brackets... etc

# Note: We need to use a queue, since we want to push try all strings with 1 bracket
# removed before we try any of the strings with 2 brackets removed, etc.

# Note #2: We should also use a hashtable to prevent duplicates.
# Runtime: O(n * 2^n), since there are 2^n possible subsets of brackets and it takes
# O(n) time to check if they are valid.

# Note #3: In order to get AC on LeetCode, we need to make sure we only add elements
# to the queue once. So make sure that everytime you generate a subset, you also add it to
# the hashtable. Don't queue elements that are already in the hashtable.
from collections import deque
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Helper function for checking if s is valid
        def isValid(s):
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        ans = []
        lookup = {s:False}
        queue = deque([s])
        while len(queue) > 0:
            s = queue.popleft()
            if isValid(s):
                if lookup[s] == False:
                    ans.append(s)
                    lookup[s] = True
            elif len(ans) == 0:
                # Try removing every possible bracket
                for i in range(len(s)):
                    if s[i] == "(" or s[i] == ")":
                      s2 = s[0:i]+s[i+1:]
                      if s2 not in lookup:
                        queue.append(s[0:i]+s[i+1:])
                        lookup[s2] = False
        return ans