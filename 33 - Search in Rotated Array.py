# Solution 1: Do a normal binary search, but add extra conditions for checking
# which direction you need to go
class Solution(object):
    def rotatedBinarySearch(self,nums,target,low,high,prev):
        middle = int((high+low)/2)
        if nums[middle] == target:
            return middle
        if middle == prev:
            return -1
        condition1 = nums[high] > nums[middle] and target > nums[middle] and target <= nums[high]
        condition2 = nums[high] < nums[middle] and (target < nums[low] or target > nums[middle-1])
        # Check if value is on right side
        if condition1 or condition2:
            # Go right
            return self.rotatedBinarySearch(nums,target,middle+1,high,middle)
        # Go left
        return self.rotatedBinarySearch(nums,target,low,middle,middle)
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        return self.rotatedBinarySearch(nums,target,0,len(nums)-1,None)

# Solution 2: Speed up the binary search by getting rid of the recursion
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        low = 0
        high = len(nums)-1
        while low < high:
            middle = int((low+high)/2)
            if nums[middle] == target:
                return middle
            condition1 = nums[high] > nums[middle] and target > nums[middle] and target <= nums[high]
            condition2 = nums[high] < nums[middle] and (target < nums[low] or target > nums[middle-1])
            if condition1 or condition2:
                # Go right
                low = middle+1
            else:
                # Go left
                high = middle
        if target == nums[high]:
            return high
        return -1
