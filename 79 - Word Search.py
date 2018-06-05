# Solution 1: My first attempt at a solution here was to do a brute force DFS
# starting from every possible start node. While this works, the time complexity
# is exponential since we keep track of every visited node using deepcopy
# on each recursion. This results in exponential time and space complexity.

import copy
class Solution(object):
    def recursiveCheck(self, board, word, visited, i, j):
        visited[(i,j)] = True # mark the current location as visited
        # Base case
        if len(word) == 1:
            return True
        nextChar = word[1]
        # Go left
        if i-1 >= 0 and (i-1,j) not in visited and board[i-1][j] == nextChar:
            if self.recursiveCheck(board,word[1:],copy.deepcopy(visited),i-1,j):
                return True
        # Go right
        if i+1 < len(board) and (i+1,j) not in visited and board[i+1][j] == nextChar:
            if self.recursiveCheck(board,word[1:],copy.deepcopy(visited),i+1,j):
                return True
        # Go down
        if j-1 >= 0 and (i,j-1) not in visited and board[i][j-1] == nextChar:
            if self.recursiveCheck(board,word[1:],copy.deepcopy(visited),i,j-1):
                return True
        # Go up
        if j+1 < len(board[0]) and (i,j+1) not in visited and board[i][j+1] == nextChar:
            if self.recursiveCheck(board,word[1:],copy.deepcopy(visited),i,j+1):
                return True
        return False
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        possible = [] # list of possible starting points
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    possible.append((i,j))
        for indices in possible:
            if self.recursiveCheck(board,word,{},indices[0],indices[1]):
                return True
        return False


# Solution 2: You can get rid of deepcopy by REMOVING the
# visited key from the dict on failed paths. Now we have O(m*n) time complexity.
class Solution(object):
    def recursiveCheck(self, board, word, visited, i, j):
        visited[(i,j)] = True # mark the current location as visited
        # Base case
        if len(word) == 1:
            return True
        nextChar = word[1]
        # Go left
        if i-1 >= 0 and (i-1,j) not in visited and board[i-1][j] == nextChar:
            if self.recursiveCheck(board,word[1:],visited,i-1,j):
                return True
        # Go right
        if i+1 < len(board) and (i+1,j) not in visited and board[i+1][j] == nextChar:
            if self.recursiveCheck(board,word[1:],visited,i+1,j):
                return True
        # Go down
        if j-1 >= 0 and (i,j-1) not in visited and board[i][j-1] == nextChar:
            if self.recursiveCheck(board,word[1:],visited,i,j-1):
                return True
        # Go up
        if j+1 < len(board[0]) and (i,j+1) not in visited and board[i][j+1] == nextChar:
            if self.recursiveCheck(board,word[1:],visited,i,j+1):
                return True
        visited.pop((i,j), None) # failed path, remove the visited location
        return False
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        possible = [] # list of possible starting points
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    possible.append((i,j))
        for indices in possible:
            if self.recursiveCheck(board,word,{},indices[0],indices[1]):
                return True
        return False

# Solution 3: We can further speed up our solution by removing the visited dict.
# We can do this by temporary changing the value of board tiles, and
# changing it back if the path fails.
class Solution(object):
    def recursiveCheck(self, board, word, i, j):
        tmp = board[i][j]
        board[i][j] = -1 # mark the char as visited
        # Base case
        if len(word) == 1:
            return True
        nextChar = word[1]
        # Go left
        if i-1 >= 0 and board[i-1][j] == nextChar:
            if self.recursiveCheck(board,word[1:],i-1,j):
                return True
        # Go right
        if i+1 < len(board) and board[i+1][j] == nextChar:
            if self.recursiveCheck(board,word[1:],i+1,j):
                return True
        # Go down
        if j-1 >= 0 and board[i][j-1] == nextChar:
            if self.recursiveCheck(board,word[1:],i,j-1):
                return True
        # Go up
        if j+1 < len(board[0]) and board[i][j+1] == nextChar:
            if self.recursiveCheck(board,word[1:],i,j+1):
                return True
        board[i][j] = tmp # failed path, put the char back
        return False
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        possible = [] # list of possible starting points
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    possible.append((i,j))
        for indices in possible:
            if self.recursiveCheck(board,word,indices[0],indices[1]):
                return True
        return False



