# Solution 1: Make a skyline array from min(left side of buildings) to
# max(right side of buildings).
# Then skyline[i] = max(height of all buildings that exist at i)

# Runtime: O(# of buildings * building range)
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) == 0:
            return buildings
        left = buildings[0][0]
        right = buildings[0][1]
        for building in buildings:
            left = min(left, building[0])
            right = max(right, building[1])
        skyline = [0 for x in range(left,right)]
        # Build the skyline
        for building in buildings:
            for i in range(building[0],building[1]):
                skyline[i-left] = max(skyline[i-left],building[2])
        # Build our answer from the skyline
        ans = [[left,skyline[0]]]
        for i in range(1, len(skyline)):
            if skyline[i] != skyline[i-1]:
                ans.append([i+left,skyline[i]])
        ans.append([right,0])
        return ans

# Solution 2: Observe that the skyline can only change at the start and end of each building.
# With this in mind, we can represent buildings as "critical points", where there is one
# critical point for the top left of each building and one for the bottom right.
# Then for each critical point, we change the point's height to be that of the highest building
# covering the critical point.

# To get our answer, we iterate over the "critical point" array and output every time the
# height changes. Runtime = O(n^2)
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) == 0:
            return buildings
        cPoints = []
        for building in buildings:
            # Append top left of building as a critical point
            cPoints.append([building[0],building[2]])
            # Append bottom right of building as a critical point
            cPoints.append([building[1],0])
        # Maximize the height of each cPoint
        for c in cPoints:
            for building in buildings:
                if c[0] >= building[0] and c[0] < building[1]:
                    c[1] = max(c[1],building[2])
        # Build our answer from the cPoints
        ans = [cPoints[0]]
        cPoints.sort()
        for i in range(1, len(cPoints)):
            if cPoints[i][1] != cPoints[i-1][1]:
                ans.append(cPoints[i])
        return ans

# Solution 3: Observe that for each critical point, we just need the tallest building above it.
# If we can get this building in faster than O(n), we'll have beat our previous solution!

# Let's use a max heap to keep track of the tallest building. When we hit the left edge of
# a building, add it to the heap. At the right edge of the building, remove it from the heap.
# When we hit a critical point, the tallest building currently above it is simply the top of the heap.
# Runtime: O(nlogn)
import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) == 0:
            return buildings
        cPoints = []
        for building in buildings:
            # Append top left of building as a critical point
            cPoints.append([building[0],building[2]])
            # Append bottom right of building as a critical point
            cPoints.append([building[1],0])
        cPoints.sort()
        # Maximize the height of each cPoint
        heap = [] # max heap keeps track of <height of building, right side of building>
        index = 0
        for point in cPoints:
            # Remove all buildings from the heap that we've passed
            while len(heap) > 0 and point[0] >= heap[0][1]:
                heapq.heappop(heap)
            # Add all buildings we've caught up to
            while index < len(buildings) and buildings[index][0] <= point[0]:
                 heapq.heappush(heap,(-1*buildings[index][2],buildings[index][1]))
                 index += 1
            # Maximize the cPoint
            if len(heap) > 0:
                point[1] = max(point[1],-1*heap[0][0])
        # Build our answer from the cPoints
        ans = [cPoints[0]]
        for i in range(1, len(cPoints)):
            if cPoints[i][1] != cPoints[i-1][1]:
                ans.append(cPoints[i])
        return ans