# Solution 1: O(n) runtime and O(1) space
# Swap every number into the position it belongs in the array
# If the number is outside the array bounds, set it to -1 and keep going
# If the number is a duplicate inside the array bounds, set it to -1 and keep going
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Edge cases
        if len(nums) == 0:
            return 1
        elif len(nums) == 1 and nums[0] == 1:
            return 2
        nums.append(0)
        duplicates = set()
        # Place every integer into the position it belongs in the array
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            elif nums[i] >= len(nums) or nums[i] <= 0 or nums[i] in duplicates:
                nums[i] = -1
                i += 1
            else:
                duplicates.add(nums[i])
                self.swap(nums, i, nums[i])
        for i in range(1, len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
            
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp