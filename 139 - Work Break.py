# Solution 1: Brute force
class Solution(object):
    def recursiveCheck(self, s, lookup):
        if len(s) == 0:
            return True
        if s[0] not in lookup:
            return False
        for word in lookup[s[0]]:
            if len(word) <= len(s) and word == s[0:len(word)] and self.recursiveCheck(s[len(word):], lookup):
                return True
        return False
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        lookup = {}
        for word in wordDict:
            if word[0] in lookup:
                lookup[word[0]].append(word)
            else:
                lookup[word[0]] = [word]
        if s[0] not in lookup:
            return False
        start = lookup[s[0]]
        for word in start:
            if len(word) <= len(s) and word == s[0:len(word)] and self.recursiveCheck(s[len(word):], lookup):
                return True
        return False

# Solution 2: Add memoization, AC's on LeetCode
class Solution(object):
    def recursiveCheck(self, s, lookup, memo):
        if len(s) == 0:
            return True
        if s[0] not in lookup:
            memo[s] = False
            return False
        for word in lookup[s[0]]:
            if word not in memo and len(word) <= len(s) and word == s[0:len(word)] and self.recursiveCheck(s[len(word):], lookup, memo):
                return True
            else:
                memo[s] = False
        memo[s] = False
        return False
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        lookup = {}
        for word in wordDict:
            if word[0] in lookup:
                lookup[word[0]].append(word)
            else:
                lookup[word[0]] = [word]
        if s[0] not in lookup:
            return False
        start = lookup[s[0]]
        for word in start:
            if len(word) <= len(s) and word == s[0:len(word)] and self.recursiveCheck(s[len(word):], lookup, {}):
                return True
        return False

# Solution 3: Dynamic programming 
class Solution(object):
    def wordBreak(self, s, words):
        dp = [False for x in range(len(s)+1)]
        dp[0] = True # can always make an empty string
        # dp[i] = True if we could make everything up i-len(word) and the word matches the string
        # after i-len(word):i
        for i in range(len(dp)):
            for word in words:
                if i-len(word) >= 0 and dp[i-len(word)] and word == s[i-len(word):i]:
                    dp[i] = True
        return dp[-1]

