# Solution 1: Just follow the logic they give you
# Runtime: O(V*len(heights))

import math
class Solution:
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        for raining in range(V):
            low = heights[K]
            low_index = -1
            # Try going left
            for i in range(K-1,-1,-1):
                if heights[i] > low:
                    break
                if heights[i] < low:
                    low = heights[i]
                    low_index = i
            if low_index > -1:
                heights[low_index] += 1
                continue
            # Try going right
            for i in range(K+1,len(heights)):
                if heights[i] > low:
                    break
                if heights[i] < low:
                    low = heights[i]
                    low_index = i
            if low_index > -1:
                heights[low_index] += 1
                continue
            # Raise current
            heights[K] += 1
        return heights