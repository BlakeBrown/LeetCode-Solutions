# Solution 1: Idea is to use dynamic programming.
# Nums[i] = product of numbers to the left i * product of numbers to the right of i

# O(n) time and O(n) space
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1 for x in range(len(nums))] # left[i] = product of numbers to the left of i
        right = [1 for x in range(len(nums))] # right[i] = product of numbers to the right of i
        for i in range(1,len(nums)):
            left[i] = left[i-1] * nums[i-1]
            right[-i-1] = right[-i] * nums[-i]
        for i in range(0,len(nums)):
            nums[i] = left[i]*right[i]
        return nums
        