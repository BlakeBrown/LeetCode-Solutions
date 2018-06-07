# Solution 1: Compute the sum of every subarray
# Runtime: O(n^2)
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxCount = 0
        for i in range(0,len(nums)):
            total = nums[i]
            count = 1
            if total == k and count > maxCount:
                maxCount = count
            for j in range(i+1,len(nums)):
                total += nums[j]
                count += 1
                if total == k and count > maxCount:
                    maxCount = count
        return maxCount
                
# Solution 2: Use dynamic programming
# Runtime: O(n)

# Basic idea is to sum every # and store the size of the effective subarray in a hashtable
# As we go through the array, we can change the value of k that we're looking for to
# reflect "removing" an item from our initial subarrays
# ex. nums = [1,2,3,4,5]
# 
# lookup = {1:1, 3:2, 6:3, 10:4, 15:5}

# k = 12
# k in lookup? no
# k += 1
# next

# k = 13
# k in lookup? no
# k += 2
# next

# k = 15
# k in lookup? yes
# lookup[15] = 5, but we've already removed 1 and 2 from our subarray
# so we return 5-2 = 3

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lookup = {}
        count = 0
        for i in range(0,len(nums)):
            count += nums[i]
            lookup[count] = i +1
        maxLength = 0
        for i in range(0,len(nums)):
            if k in lookup and lookup[k]-i > maxLength:
                maxLength = lookup[k]-i
            k += nums[i]
        return maxLength










