class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        highest_right = [0] * len(height)
        highest_left = [0] * len(height)
        # Compute highest left
        for i in range(1, len(height)):
            highest_left[i] = max(height[i-1], highest_left[i-1])
        # Compute highest right
        for i in range(len(height)-2,-1,-1):
            highest_right[i] = max(height[i+1], highest_right[i+1])
        # Compute rain
        rain = 0
        for i in range(len(height)):
            rain += max(min(highest_left[i],highest_right[i])-height[i],0)
        return rain