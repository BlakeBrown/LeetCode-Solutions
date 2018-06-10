# Solution 1: TLE's
# Use sets to eliminate non-celebs, runtime is O(n^2)

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        potentialCelebs = set(i for i in range(n))
        nodeKnows = set()
        doesntKnowNode = set()
        while(len(potentialCelebs) > 0):
            node = next(iter(potentialCelebs))
            for i in range(0,n):
                if i == node:
                    continue
                if knows(node,i):
                    nodeKnows.add(i)
                if not knows(i,node):
                    doesntKnowNode.add(i)
            if len(nodeKnows) == 0 and len(doesntKnowNode) == 0:
                return node
            potentialCelebs &= nodeKnows
            potentialCelebs &= doesntKnowNode
            nodeKnows = set()
            doesntKnowNode = set()
        return -1

# Solution 2: Use sets w/ lookup table, still TLE's :'(
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        lookup = {}
        potentialCelebs = set(i for i in range(n))
        nodeKnows = set()
        doesntKnowNode = set()
        while(len(potentialCelebs) > 0):
            node = next(iter(potentialCelebs))
            for i in range(0,n):
                if i == node:
                    continue
                if (node,i) not in lookup:
                    if knows(node,i):
                        nodeKnows.add(i)
                        lookup[(node,i)] = True
                    else:
                        lookup[(node,i)] = False
                elif lookup[(node,i)]:
                    nodeKnows.add(i)
                if (i,node) not in lookup:
                    if not knows(i,node):
                        lookup[(i,node)] = False
                        doesntKnowNode.add(i)
                    else:
                        lookup[(i,node)] = True
                elif not lookup[(i,node)]:
                    doesntKnowNode.add(i)
            if len(nodeKnows) == 0 and len(doesntKnowNode) == 0:
                return node
            potentialCelebs &= nodeKnows
            potentialCelebs &= doesntKnowNode
            nodeKnows = set()
            doesntKnowNode = set()
        return -1

# Solution 3: Let's do something more clever. This problem is the same as finding
# a "universal sink" in a graph. To find a universal sink, first find any sink in the
# graph. If this sink is a universal sink, we found the universal sink, otherwise there
# is no universal sink in the graph.

# O(n) runtime, O(n) space
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        visited = set()
        node = 0
        while len(visited) < n:
            visited.add(node)
            sink = True
            for i in range(0, n):
                if i == node:
                    continue
                if i not in visited and knows(node,i):
                    # Visit i
                    node = i
                    sink = False
                    break
            if sink:
                # Found sink, check if it's universal
                for i in range(0,n):
                    if i == node:
                        continue
                    if not knows(i, node):
                        return -1
                    if knows(node,i):
                        return -1
                return node
        return -1

# Solution 4: Let's shorten the code and use O(1) space
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        # find any sink in the graph
        sink = 0
        for i in range(1,n):
            if knows(sink,i):
                sink = i
        # check if it's a universal sink
        for i in range(0,n):
            if i == sink:
                continue
            if not knows(i, sink):
                return -1
            if knows(sink,i):
                return -1
        return sink


















