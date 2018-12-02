# Solution 1 - First sort the array
# ex. [1,2,3,3,3,3,4,5]

# Take the median, in this case the index of the median is 3
# Place the median, than the largest number, then place the number to the left of the median,
# then the second largest number, etc.

# 3, 5, 3, 4, 2, 3, 1, 3

# This guarantees we'll be wiggled since by the time we hit the median on the right
# side, we'll have left the median on the left side. Hopefully this makes sense intuitively.

# Runtime: O(nlogn)
def wiggleSort(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    nums.sort()
    medianIndex = int((len(nums)-1)/2)
    i = 0
    ans = []
    while medianIndex - i >= 0:
        ans.append(nums[medianIndex-i])
        ans.append(nums[-1-i])
        i += 1
    for i in range(len(nums)):
        nums[i] = ans[i]

# Solution 2 - Use list slicing to speed up solution (same runtime complexity)
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        medianIndex = int((len(nums)-1)/2)
        ans = [0] * len(nums)
        ans[::2] = nums[medianIndex::-1]
        ans[1::2] = nums[:medianIndex:-1]
        for i in range(len(nums)):
            nums[i] = ans[i]

# Solution 3 - In order to get O(n) time, you need to use:
# 1. Quick select to get the median
# 2. DNF to partition the array around the median
# 3. Virtual indexing during DNF that partitions the array into exactly the places
# where the elements need to be.

# Needless to say, I don't think this is worth the time during an interview
# so I'm going to skip this solution.

# However, take a look at:
# 75 - Sort Colors for DNF
# 215 - Kth Largest for quick select

