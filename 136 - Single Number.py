class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = nums[0]
        for i in range(1,len(nums)):
            answer ^= nums[i]
        return answer