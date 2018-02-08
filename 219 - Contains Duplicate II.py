class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        indexLookup = {}
        for i, num in enumerate(nums):
            if num in indexLookup:
                if abs(i-indexLookup[num]) <= k:
                    return True
            indexLookup[num] = i
        return False