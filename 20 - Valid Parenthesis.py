class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                c2 = stack.pop()
                if c == "}" and c2 != "{":
                    return False
                if c == ")" and c2 != "(":
                    return False
                if c == "]" and c2 != "[":
                    return False
        if len(stack) != 0:
            return False
        return True