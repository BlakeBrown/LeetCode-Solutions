
# Great article on this problem: http://www.ardendertat.com/2011/10/31/programming-interview-questions-12-reverse-words-in-a-string/

# Solution 1: O(n) time and O(n) space. Let python do all the work
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(reversed(s.split()))

# Solution 2: O(n) time and O(n) space, let's do slightly more work by iterating over the string ourselves
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = ""
        # remove extra whitespace
        s = s.split()
        # edge cases
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s[0]
        s = ' '.join(s)
        # algorithm
        lastIndex = len(s)
        for index in range(len(s)-1,-1, -1):
            if s[index] == " ":
                word = s[(index+1):lastIndex]
                if lastIndex == len(s):
                    answer += word
                else:
                    answer += " " + word
                lastIndex = index
            elif index == 0:
                word = s[index:lastIndex]
                answer += " " + word
        return answer

# Solution 3: O(n) time and O(1) space.
# - We can't do this in Python, since strings are immutable.
# - However, we could do this in C or C++ by reversing every word in the string (in-place),
# and then reversing the entire string character by character.
# Why does this work? Logically you can see that reversed words will get
# re-reversed back to their correct spelling and words at the back
# of the string will get moved to the front.





