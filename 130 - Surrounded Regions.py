# Idea 1: Everytime we encounter an O on the board,
# run a DFS to convert all neighbouring O's to X's. 
# If any of these O's lies on the edge of the board,
# convert all of the O's back to X's.

# Although not shown, we could optimize this with a visited
# array to make sure we only visit every array index once. This
# would give us a runtime of O(n^2).

class Solution(object):
    def fill(self, board, i, j, modified):
        board[i][j] = "X"
        modified.append([i,j])
        if j > 0 and board[i][j-1] == "O":
            self.fill(board, i, j-1, modified)
        if j+1 < len(board[i]) and board[i][j+1] == "O":
            self.fill(board, i, j+1, modified)
        if i > 0 and board[i-1][j] == "O":
            self.fill(board, i-1, j, modified)
        if i+1 < len(board) and board[i+1][j] == "O":
            self.fill(board, i+1, j, modified)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # Edge cases
        if(len(board) != 0 and isinstance(board[0], list)):
            # Check board for O's, cross them off if they are surrounded
            for i in range(0, len(board)):
                for j in range(0, len(board[i])):
                    if(board[i][j] == "O"):
                        modified = []
                        self.fill(board,i,j,modified)
                        # Check if any of the modified squares was on the border, if 
                        # so revert them all
                        hitBorder = False
                        for k in range(0, len(modified)):
                            if modified[k][0] == 0 or modified[k][0]+1 == len(board) or modified[k][1] == 0 or modified[k][1]+1 == len(board[0]):
                                hitBorder = True
                                break
                        if hitBorder:
                            for k in range(0, len(modified)):
                                board[modified[k][0]][modified[k][1]] = "O"


# Idea #2: A better solution shown in discussions is to 
# first convert all O's on the edges of the board to another character
# such as 1's. Then we just iterate over the board and change all remaining
# O's to X's and all 1's back to O's.
