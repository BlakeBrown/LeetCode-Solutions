class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums)*(len(nums)+1)/2
        for num in nums:
            total -= num
        return total