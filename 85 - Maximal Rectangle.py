# Solution 1: Brute force, consider every point as the top left corner of a rectangle.
# Check the largest area we can make from that corner by determining the width of the
# rectangle, go to the next row (if there's another 1), decrease the width if necessary, etc.
# Runtime is O(n^4).

# Solution 2: Let's be more clever with how we check the area of a point. We can use dp to
# keep track of the number of 1's to the left of each point (including itself).
# Runtime is O(n^3) since we immediately know the width of each point, we just need
# to check the height.

# Solution 3: Let's see if we can improve our dp approach. Notice that the area of a rectangle
# is simply width*height. Can we find the width*height for a point[i][j] in O(1) time? Yes!
# If we keep track of the # of 1's to the left, AND the # of 1's to the right,
# AND the height using dp, we can iterate over all the points and solve
# the problem in O(n^2) time and O(n) space.

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        left = [[len(matrix[0]) for c in range(len(matrix[0]))] for r in matrix]
        right = [[len(matrix[0]) for c in range(len(matrix[0]))] for r in matrix]
        height = [[0 for c in range(len(matrix[0]))] for r in matrix]
        maxArea = 0
        for i in range(len(matrix)):
            count = 0
            # left[i][j] = # of 1's to the left of i,j including self
            for j in range(0,len(matrix[0])):
                if matrix[i][j] == "0":
                    count = 0
                else:
                    count += 1
                    left[i][j] = count
                    if i > 0:
                        left[i][j] = min(count,left[i-1][j])
            count = 0
            # right[i][j] = # of 1's to the right of i,j including self
            for j in range(len(matrix[0])-1,-1,-1):
                if matrix[i][j] == "0":
                    count = 0
                else:
                    count += 1
                    right[i][j] = count
                    if i > 0:
                        right[i][j] = min(count,right[i-1][j])
            # height[i][j] = # of 1's above i,j including self
            for j in range(0,len(matrix[0])):
                if matrix[i][j] == "0":
                    continue
                height[i][j] = 1
                if i > 0:
                    height[i][j] += height[i-1][j]
            for j in range(0,len(matrix[0])):
                area = (right[i][j]+left[i][j]-1)*height[i][j]
                if area > maxArea:
                    maxArea = area
        return maxArea

# Solution 4: We can improve the memory in solution 3 to O(n) by observing that we only
# use one row for dp at a time.

# Solution 5: This problem is the same as histogram https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/
# We consider the first row as our initial histogram, and when move to next row we
# consider this as adding another row to the bottom of our histogram. 
# Since the histogram solution takes O(n) time to to check a row, and we need to check every row,
# this solution is also O(n^2)
