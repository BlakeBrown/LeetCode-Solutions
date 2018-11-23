from heapq import heappush, heappop
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        # Encode the board as a 1-D array
        start = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                start.append(board[i][j])
        goal = [1,2,3,4,5,0]
        
        heap = []
        heappush(heap, (self.calculateHeuristic(start),start))
        adjacent_squares = {
            0: [1,3],
            1: [0,2,4],
            2: [1,5],
            3: [0,4],
            4: [1,3,5],
            5: [2,4]
        }
        visited = set()
        while len(heap) > 0:
            state = heappop(heap)
            board_state = state[1]
            # Check if we've hit the goal state
            if self.calculateHeuristic(board_state) == 0:
                return state[0]
            visited.add(tuple(board_state))
            g = state[0] - self.calculateHeuristic(board_state) + 1
            # Generate neighbours
            index_of_zero = board_state.index(0)
            for square in adjacent_squares[index_of_zero]:
                new_board_state = board_state[:]
                new_board_state[index_of_zero] = new_board_state[square]
                new_board_state[square] = 0
                if tuple(new_board_state) in visited:
                    continue
                h = self.calculateHeuristic(new_board_state)
                heappush(heap, (g + h, new_board_state))
        return -1
    
    # Calculates the heuristic function, ex. the # of mismatched squares
    def calculateHeuristic(self, board):
        h = 0
        if board[0] != 1:
            h += 1
        if board[1] != 2:
            h += 1
        if board[2] != 3:
            h += 1
        if board[3] != 4:
            h += 1
        if board[4] != 5:
            h += 1
        if board[5] != 0:
            h += 1
        return h