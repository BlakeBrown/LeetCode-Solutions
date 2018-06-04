# Solution 1: An O(n) solution is to maintain a count as we go through the array.
# Everytime the count is bigger than our max count, we've found a new maximum subarray.
# Everytime the count goes negative, we reset to the count to 0
# (effectively make a new subarray).

# The reason I like my solution in this form is that it's very easy to return the elements
# of the subarray if an interviewer asked for them.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return nums
        start = 0
        end = 0
        count = 0
        maxStart = 0
        maxEnd = 0
        maxCount = None
        for i in range(len(nums)):
            count += nums[i]
            if maxCount is None or count > maxCount:
                maxCount = count
                maxStart = start
                maxEnd = i
            if count < 0:
                # No point in continuing the subarray, so we start over
                start = i+1
                count = 0
        return sum(nums[maxStart:maxEnd+1])