# Solution #1: This is the first solution I came up with, 
# it involves making a graph and then performing a BFS on the graph.
# While this solution times out on LeetCode, it's a great starting
# point for understanding how to solve the problem.
class Node(object):
    def __init__(self):
        self.adjacentNodes = []

class Solution(object):
    # Returns True if a and b are one char apart, false otherwise
    def oneCharDiff(self, a, b):
        numDifferences = 0
        for i in range(0, len(a)):
            if a[i] != b[i]:
                numDifferences += 1
            if numDifferences > 1:
                return False
        return True

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Make a graph where each word is a node. Words that are 
        # only one character apart are connected by edge.
        wordList.append(beginWord)
        graph = {}
        for i in range(0, len(wordList)):
            graph[wordList[i]] = Node()
        for i in range(0, len(wordList)):
            for j in range(i+1, len(wordList)):
                if(self.oneCharDiff(wordList[i], wordList[j])):
                    graph[wordList[i]].adjacentNodes.append(wordList[j])
                    graph[wordList[j]].adjacentNodes.append(wordList[i])
        # Apply BFS
        distance = {} # distance[word] = # of nodes to reach word
        distance[beginWord] = 1
        queue = [beginWord]
        while len(queue) != 0:
            # Pop front of queue
            front = queue.pop(0)
            # Add adjacent nodes to the queue
            for i in range(0, len(graph[front].adjacentNodes)):
                if graph[front].adjacentNodes[i] not in distance:
                    distance[graph[front].adjacentNodes[i]] = distance[front] + 1
                    queue.append(graph[front].adjacentNodes[i])
        if endWord not in distance:
            return 0
        else:
            return distance[endWord]

# Solution #2: Let's make an optimization on the first solution.
# Note that constructing the graph takes O(V^2) time where
# V is number of nodes (words) in the graph. We can eliminate this cost 
# by "making" the graph as we do the BFS. For example, the only
# nodes that could be connected to "hit" are a-z + i + t, 
# h + a-z + t or h + i + a-z. This takes only 81 iterations
# to generate all possible children for each node we visit in the BFS.
# We could say this takes constant time with respect to the input,
# and we completely eliminate the cost of constructing the graph up front.
class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordDict = {}
        for word in wordList:
            wordDict[word] = True
        # Apply BFS
        distance = {} # distance[word] = # of nodes to reach word
        distance[beginWord] = 1
        queue = [beginWord]
        while len(queue) != 0:
            # Pop front of queue
            front = queue.pop(0)
            # Find all children of front by generating all possible
            # children and checking if any of them exist
            children = []
            for i in range(0, len(front)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    possibleChild = front[:i] + c + front[i+1:]
                    if possibleChild in wordDict:
                        children.append(possibleChild)
            # Add adjacent nodes to the queue
            for i in range(0, len(children)):
                if children[i] not in distance:
                    distance[children[i]] = distance[front] + 1
                    queue.append(children[i])
        if endWord not in distance:
            return 0
        else:
            return distance[endWord]

# Solution #3 (unidirectional BFS with sets):
# We can further optimize the previous solution by 
# doing a bidirectional BFS. To set up for this, start by changing
# our BFS to use sets. The reason we need to use sets is because
# bidirectional BFS requires us to compare beginQueue with
# endQueue on each iteration. Sets are much faster to compare than lists.
# See: https://wiki.python.org/moin/TimeComplexity

class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Apply BFS with sets.
        wordSet = set(wordList) # O(n) time to make set
        front = set([beginWord])
        distance = 1
        while len(front) != 0:
            # Generate all possible children of the nodes in front
            possible = set(word[:i] + c + word[i+1:] for word in front for i in range(0, len(word)) for c in 'abcdefghijklmnopqrstuvwxyz')
            # Take the intersection with wordSet to get the next children
            # we want to visit
            front = wordSet & possible
            distance += 1
            wordSet -= front
            if endWord in front:
                return distance
        return 0

# Solution #4 (bidirectional BFS with): This is much faster than our
# previous solutions since it applies BFS in both directions.
class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        back = set([endWord])
        front = set([beginWord])
        distance = 1
        # Edge case
        if endWord not in wordSet:
            return 0
        # Apply bidirectional BFS
        while len(front) != 0:
            # Take the intersection of sets to see if we've found a 
            # common node. We need to do this at the start of the loop
            # in case back = front.
            if front & back:
                return distance
            # Remove nodes we've already visited to avoid a cycle
            wordSet -= front
            # Generate all possible children of the nodes in front
            possible = set(word[:i] + c + word[i+1:] for word in front for i in range(0, len(word)) for c in 'abcdefghijklmnopqrstuvwxyz')
            front = wordSet & possible
            distance += 1
            # Swap back and front. This is so on the next iteration
            # we're expanding from the destination, and the iteration after
            # after we're expanding from the source, and so on.
            # This is the key part of bidirectional BFS.
            tmp = front
            front = back
            back = tmp
        return 0
