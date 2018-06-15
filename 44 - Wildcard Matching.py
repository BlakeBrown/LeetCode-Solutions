# Solution 1: Dynamic programming with O(n*s) runtime and O(n*s) space
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Edge case
        if len(s) == 0:
            for c in p:
                if c != "*":
                    return False
            return True
        matrix = [[False for c in range(len(s)+1)] for r in range(len(p)+1)]
        matrix[0][0] = True # can always match empty string
        for i in range(1,len(p)+1):
            for j in range(1,len(s)+1):
                if p[i-1] == "?":
                    matrix[i][j] = matrix[i-1][j-1] # automatic match
                elif p[i-1] == "*":
                    k = 0
                    while k < len(s)+1 and not matrix[i-1][k]:
                        k += 1
                    # If we found a match without the *, we can match the rest of the string
                    for l in range(k,len(s)+1):
                        matrix[i][l] = True
                    break
                else:
                    # Letter is normal char
                    if p[i-1] == s[j-1] and matrix[i-1][j-1]:
                        matrix[i][j] = True
                    else:
                        matrix[i][j] = False
        return matrix[-1][-1]