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
