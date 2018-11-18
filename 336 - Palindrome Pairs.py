# Solution 1: Brute force, find all palindromes
class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if self.isPalindrome(words[i] + words[j]):
                    ans.append([i,j])
        return ans

    def isPalindrome(self, word):
        for i in range(0, int(len(word)/2)):
            if word[i] != word[-i-1]:
                return False
        return True



# Solution 2: Cache the solutions. Worst-case runtime is still O(len(words)^2 * average word length). TLE's.
class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ans = []
        cache = {}
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                combined = words[i] + words[j]
                if combined not in cache:
                    cache[combined] = self.isPalindrome(words[i] + words[j])
                if cache[combined]
                    ans.append([i,j])
        return ans

    def isPalindrome(self, word):
        for i in range(0, int(len(word)/2)):
            if word[i] != word[-i-1]:
                return False
        return True


# I was stuck so I read https://fizzbuzzed.com/top-interview-questions-5/

# We can change the runtime to O(average word length ^ 2 * len(words)) when len(words) >> average word length

# Consider abcdxx, dcba, abcd, ydcba, xxdcba

# Let's think about the pairs we can make

# Case 1: abcdxx + dcba = abcd | xx | dcba = s1 + palindromic suffix + s2
# We split word 1 to make a pair

# Case 2: abcd + ydcba = abcd | y | dcba = s1 + palindromic prefix + s2
# We split word 2 to make a pair

# To handle case 1, check if we have:
# "" as a word? no
# "a" as a word? no
# "ba" as a word? no
# "cba" as a word? no
# "dcba" as a word? yes. Is the rest of string "xx" a palindrome? yes. so we have a solution.
# "xdcba" as a word? no
# "xxdcba" as a word? yes. Is the rest of the string "" a palindrome? yes. so we have a solution.

# Case 2 is the same as case 1 but we reverse the word.

# Use a set to avoid creating duplicate solutions

class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ans = []
        cache = {}
        solutions = set()
        for i in range(len(words)):
            cache[words[i]] = i
        # Case 1
        for i in range(len(words)):
            word = words[i]
            for j in range(len(word)+1):
                subword = word[:j]
                reversed_subword = subword[::-1]
                if reversed_subword in cache and cache[reversed_subword] != i and self.isPalindrome(word[j:]):
                    solution = (i,cache[reversed_subword])
                    solutions.add(solution)
                    ans.append(list(solution))
        # Case 2
        for i in range(len(words)):
            word = words[i]
            word = word[::-1]
            for j in range(len(word)+1):
                subword = word[:j]
                if subword in cache and cache[subword] != i and self.isPalindrome(word[j:]):
                    solution = (cache[subword],i)
                    if solution not in solutions:
                        ans.append([cache[subword], i])
        return ans

    def isPalindrome(self, word):
        for i in range(0, int(len(word)/2)):
            if word[i] != word[-i-1]:
                return False
        return True
