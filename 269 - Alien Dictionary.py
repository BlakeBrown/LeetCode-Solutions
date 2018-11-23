class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if len(words) == 0:
            return ""
        if len(words) == 1:
            return words[0]
        self.nodes = {} # letter -> next letter
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            j = 0
            for c in word1:
                if c not in self.nodes:
                    self.nodes[c] = []
            for c in word2:
                if c not in self.nodes:
                    self.nodes[c] = []
            while j < len(word1) and j < len(word2) and word1[j] == word2[j]:
                j += 1
            if j < len(word1) and j < len(word2):
                letter1 = word1[j]
                letter2 = word2[j]
                self.nodes[letter1].append(letter2)
        # Now we've built the graph, do a topological sort
        # From https://en.wikipedia.org/wiki/Topological_sorting
        # visited == -1 -> unmarked
        # visited == 0 -> temporary mark (used for detecting cycles)
        # visited == 1 -> permanently mark (don't revisit)
        self.ans = ""
        self.visited = {}
        for key in self.nodes.keys():
            self.visited[key] = -1
        for key in self.nodes.keys():
            if self.visited[key] == -1:
                if not self.visit(key):
                    return "" # Not a DAG
        return self.ans
    def visit(self, key):
        if self.visited[key] == 1:
            return True
        if self.visited[key] == 0:
            return False # Not a DAG
        self.visited[key] = 0
        for node in self.nodes[key]:
            if not self.visit(node):
                return False
        self.visited[key] = 1
        self.ans = key + self.ans
        return True

