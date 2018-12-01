# Solution 1 - Sort and swap every other index that isn't wiggle sorted
# Runtime: O(nlogn)
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        i = 1
        while i+1 < len(nums):
            if nums[i] < nums[i+1]:
                self.swap(nums, i, i+1)
            i += 2
                
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

# Solution 2 - Observe that the greedy solution works
# Let's say we have array that is already wiggly sorted up to, but not including, index i

# What can we do to nums[i] in order to be wiggly sorted?

# We have two cases:

# 1. i is odd
# In this case, nums[i-1] <= nums[i-2]
# If nums[i] >= nums[i-1], perfect nums[i] is already wiggly sorted
# If nums[i] < nums[i-1] <= nums[i-2] (by default),
# we can swap nums[i] with nums[i-1]and we'll be wiggly sorted!

# 2. i is even
# In this case, nums[i-1] >= nums[i-2]
# If nums[i] <= nums[i-1], perfect nums[i] is already wiggly sorted
# If nums[i] > nums[i-1] >= nums[i-2] (by default),
# we can swap nums[i] with nums[i-1] and we'll be wiggly sorted!
# Runtime: O(n)

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            odd = i & 1
            if odd and nums[i] < nums[i-1]:
                self.swap(nums, i, i-1)
            elif not odd and nums[i] > nums[i-1]:
                self.swap(nums, i, i-1)
                
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
