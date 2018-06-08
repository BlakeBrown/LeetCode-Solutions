class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0
        while i < len(s):
            # Check for the 4 subtraction cases
            subtract = False
            if i+1 < len(s):
                if s[i] == "I" and s[i+1] == "V":
                    res += 4
                    subtract = True
                elif s[i] == "I" and s[i+1] == "X":
                    res += 9
                    subtract = True
                elif s[i] == "X" and s[i+1] == "L":
                    res += 40
                    subtract = True
                elif s[i] == "X" and s[i+1] == "C":
                    res += 90
                    subtract = True
                elif s[i] == "C" and s[i+1] == "D":
                    res += 400
                    subtract = True
                elif s[i] == "C" and s[i+1] == "M":
                    res += 900
                    subtract = True
            if subtract:
                i += 2
                continue
            # Otherwise just add
            if s[i] == "I":
                res += 1
            elif s[i] == "V":
                res += 5
            elif s[i] == "X":
                res += 10
            elif s[i] == "L":
                res += 50
            elif s[i] == "C":
                res += 100
            elif s[i] == "D":
                res += 500
            elif s[i] == "M":
                res += 1000
            i += 1
        return res