class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix
        ans = []
        direction = 0
        i = 0
        j = 0
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False for c in range(n)] for r in range(m)]
        # print(visited)
        for k in range(m*n):
            ans.append(matrix[i][j])
            visited[i][j] = True
            candidate_i, candidate_j = self.move(i, j, direction)
            if candidate_i == m or candidate_j == n or visited[candidate_i][candidate_j]:
                # Update direction & recalculate
                direction += 1
                if direction == 4:
                    direction = 0
                candidate_i, candidate_j = self.move(i, j, direction)
            i = candidate_i
            j = candidate_j
        return ans
    def move(self, i, j, direction):
        if direction == 0:
            # Move right
            return i, j+1
        elif direction == 1:
            # Move down
            return i+1, j
        elif direction == 2:
            # Move left
            return i, j-1
        else:
            # Move up
            return i-1, j
