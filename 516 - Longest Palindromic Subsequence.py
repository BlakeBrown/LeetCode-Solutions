# Solution 1: This problem reduces down to LCS (longest common subsequence).

# You can google this or see my solution to LeetCode problem #583.
# Runs in O(len(s)^2) time and O(len(s)) space.
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
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return len(s)
        return self.LCS(s,s[::-1])