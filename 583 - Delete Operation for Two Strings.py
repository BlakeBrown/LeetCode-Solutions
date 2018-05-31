# Solution 1: Let's simplify the problem by reducing it to LCS
# (longest common subsequence). Notice if we have the LCS of
# two words, we immediately know how many characters we need to delete.

# Ex. LCS("cats", "catanddogs") = "ats" or 3
# So the number of characters we need to delete is 4 + 10 - 2*3 = 7

# The easiest way to solve LCS is a recursive solution that runs in O(2^max(word1,word2))
class Solution(object):
    # Helper function to find longest common subsequence
    def LCS(self, word1, word2):
        dp = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len(word1)][len(word2)]
                
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return len(word1) + len(word2) - self.LCS(word1, word2)*2


# Solution 2: We can use dynamic programming to reduce our LCS function to O(word1*word2)
# This requires an additional O(word1*word2) amount of memory.

# Consider LCS("cats", "catanddogs")

# We can construct a 2D dp array where dp[i][j] = the LCS for word1[0:i] and word2[0:j]

#   catanddogs
#   ----------
# c|1111111111
# a|1222222222
# t|1233333333
# s|1233333334

# If word1[i] == word2[j], then we've found a longer LCS and the rest of the row will be
# 1 + dp[i-1][j-1]

# If word2[i] != word2[j], then our LCS is the length of max(dp[i-1][j], dp[i][j-1])

# Add a row/column of 0's to prevent IndexOutOfBounds exceptions

#   "execution
#   ----------
# "|0000000000
# i|0000000111
# n|0000000112
# t|0000001112
# e|0111111112
# n|0111111112
# t|0111112222
# i|0111112333
# o|0111112344
# n|0111112345

class Solution(object):
    # Helper function to find longest common subsequence
    def LCS(self, word1, word2):
        dp = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    newLCS = 1 + dp[i-1][j-1]
                    for k in range(j, len(word2)+1):
                        dp[i][k] = newLCS
                    continue
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len(word1)][len(word2)]
                
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return len(word1) + len(word2) - self.LCS(word1, word2)*2


# Solution #3: We can reduce our memory usage to O(word1) by observing
# that on each iteration we only require the most recent row in the matrix
class Solution(object):
    # Helper function to find longest common subsequence
    def LCS(self, word1, word2):
        dp = [0 for i in range(len(word2)+1)]
        for i in range(1, len(word1)+1):
            beforeChange = 0
            for j in range(1, len(word2)+1):
                tmp = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = 1 + beforeChange
                else:
                    dp[j] = max(dp[j], dp[j-1])
                beforeChange = tmp
        return dp[len(word2)]
                
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return len(word1) + len(word2) - self.LCS(word1, word2)*2

