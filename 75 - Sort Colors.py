# Solution 1: DNF - Dutch National Flag Problem

# We can solve this in O(n) time and O(1) memory using the following algorithm
# i - keeps track of 0's
# k - keeps track of 2's
# j is the element we are comparing

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums)-1
        while j <= k:
            if nums[j] == 0:
                self.swap(nums, i, j)
                i += 1
                j += 1
            elif nums[j] == 2:
                self.swap(nums,j,k)
                k -= 1
            else:
                j += 1
            
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

# Solution 2: If you want to make it slightly faster, we can remove the swap since
# we know what the values will be
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums)-1
        while j <= k:
            if nums[j] == 0:
                nums[j] = nums[i]
                nums[i] = 0
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[j] = nums[k]
                nums[k] = 2
                k -= 1
            else:
                j += 1