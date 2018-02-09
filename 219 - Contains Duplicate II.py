class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Rather than storing the index in the hashtable, could also
        # delete the i-k key from the hashtable as you iterate
        indexLookup = {}
        for i, num in enumerate(nums):
            if num in indexLookup:
                if abs(i-indexLookup[num]) <= k:
                    return True
            indexLookup[num] = i
        return False