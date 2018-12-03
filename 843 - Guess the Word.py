# Solution 1: Guess a random word, afterwords prune all invalid words from the list
# Try guessing up to 10 times

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

import random
class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        random.seed()
        for attempt in range(10):
            # Guess
            guess = wordlist[random.randint(0, len(wordlist)-1)]
            matches = master.guess(guess)
            if matches == 6:
                return guess
            # Prune invalid answers
            i = 0
            while i < len(wordlist):
                if self.common(wordlist[i], guess) != matches:
                    wordlist.pop(i)
                else:
                    i += 1
    def common(self, word1, word2):
        common = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                common += 1
        return common

# Solution 2: In order to maximize the pruning, note how pruning works.
# We can only remove words that don't have the same # of matches as our guess.

# So what is the most common number of matches we will get from our guess?
# There is a (25/26)^6 = ~80% chance we pick all wrong letters.
# So we have a high likelyhood we get zero matches.

# In this case, it would be nice if the word we guessed had a minimum number of overlap
# with the rest of the list so we can prune as much as possible. Ideally, we pick
# the word with the minimum number of common = 0 overlap each time.

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        for attempt in range(10):
            # Guess the word with min # of common = 0 overlap
            guesses = []
            for i in range(len(wordlist)):
                overlap = 0
                for j in range(len(wordlist)):
                    if j == i:
                        continue
                    if self.common(wordlist[i], wordlist[j]) == 0:
                        overlap += 1
                guesses.append((overlap,wordlist[i]))
            guesses.sort()
            guess = guesses[0][1]
            matches = master.guess(guess)
            if matches == 6:
                return guess
            # Prune invalid answers
            i = 0
            while i < len(wordlist):
                if self.common(wordlist[i], guess) != matches:
                    wordlist.pop(i)
                else:
                    i += 1
    def common(self, word1, word2):
        common = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                common += 1
        return common



        