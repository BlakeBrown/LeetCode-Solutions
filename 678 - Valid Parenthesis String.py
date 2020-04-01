# Best solution: O(n) time and O(1) space
# If there's no *, then we can just use an integer count:
# - If we see '(' then count++
# - If we see ')' then count --
# For a valid string: the count should never go negative and the final count should be zero.
# * can represent either '(', ')' or an empty string.
# The trick is to realize that we can try all three combinations by representing count as a range (low/high).
# - If we see '(' then low++ and high++
# - If we see ')' then low-- and high--
# - If we see '*' then low-- and high++
# Checks:
# - We need to enforce that low never goes negative. This doesn't make sense, for instance if we have a
# "*" as the first character then we can't use it as a closing brace.
# - If high ever goes negative then there's a ')' we can't match and the string is invalid
# - At the end, low should be zero. This represents no remaining opening braces at the end of the string.
class Solution:
    def checkValidString(self, s):
        low = 0
        high = 0
        for c in s:
            if c == "(":
                low += 1
                high += 1
            elif c == ")":
                low -= 1
                high -= 1
            elif c == "*":
                low -= 1
                high += 1
            low = max(low, 0)
            if(high < 0):
                return False # there's a ')' we can't match
        return low == 0
        
# Another O(n) time and O(n) space solution is to use two stacks.
# One for the open braces and one for the stars.
# When you push to the stack, don't just push the char but also push the char's index.
# When you see a closing brace, pop from the open brace stack if it's not empty. If it is empty
# then pop from the star brace stack. If the star brace stack is also empty than the string is invalid.
# And the end, we need to check that we can close all the remaining '(' braces.
# Pop from the open brace stack, and see if there's a star in the star brace stack with
# a larger index that we can use to close it. If there isn't then the string is invalid.
# If we can keep popping until the open brace stack is empty, then it's a valid string.
