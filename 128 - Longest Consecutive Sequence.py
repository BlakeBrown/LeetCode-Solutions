# Solution 1: O(n) solution is to make a set (or a hashtable) of every element in the list.
# Then for every number in the original list, find the length of the longest consecutive
# sequence it belongs to by checking and removing elements from the set/hashtable.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSet = set(nums)
        maxCount = 0
        for num in nums:
            if num not in numsSet:
                continue
            high = num+1
            low = num-1
            count = 1
            while high in numsSet:
                count += 1
                numsSet.remove(high)
                high += 1
            while low in numsSet:
                count += 1
                numsSet.remove(low)
                low -= 1
            numsSet.remove(num)
            if count > maxCount:
                maxCount = count
        return maxCount