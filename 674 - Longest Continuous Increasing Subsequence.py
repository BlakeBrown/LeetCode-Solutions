# O(n) time algorithm: Move forward through the array and
# check every pair of elements. If the next element is greater
# than the current one, increment the length of the LCIS.
# Otherwise reset the LCIS to 1. Keep track of the longest LCIS.

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) <= 1):
            return len(nums)
        index = 0
        currentLCIS = 1
        maxLCIS = 1
        while(index < len(nums)-1):
            if(nums[index] < nums[index+1]):
                currentLCIS += 1
            else:
                if(currentLCIS > maxLCIS):
                    maxLCIS = currentLCIS
                currentLCIS = 1
            index += 1
        if(currentLCIS > maxLCIS):
            maxLCIS = currentLCIS
        return maxLCIS
                