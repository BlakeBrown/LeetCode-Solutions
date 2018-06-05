# Solution 1: Move all numbers to the front and make the rest of the array 0.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        zeroes = 0
        for num in nums:
            if num != 0:
                nums[count] = num
                count += 1
            else:
                zeroes += 1
        for i in range(len(nums)-zeroes,len(nums)):
            nums[i] = 0
        

# Solution 2: We can do slightly better by just swapping, so we do everything in one pass.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                tmp = nums[count]
                nums[count] = nums[i]
                nums[i] = tmp
                count += 1
