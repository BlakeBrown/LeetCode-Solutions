class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        # First number doesn't change
        start = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
        while len(nums) > count:
            nums.pop()
        return count