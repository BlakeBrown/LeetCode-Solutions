# Solution 1: This problem is the same as finding a "universal sink" in a graph.
# A universal sink in the graph => there is no other sink in the graph, so 
# we can just iterate through the nodes until we find a sink. Then check if it's universal.

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
        # find a sink in the graph
        sink = 0
        for i in range(1,n):
            if knows(sink,i):
                sink = i
        # check if it's universal
        for i in range(0,n):
            if i == sink:
                continue
            if not knows(i, sink):
                return -1
            if knows(sink,i):
                return -1
        return sink


















