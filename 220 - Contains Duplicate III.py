class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # Edge cases
        if t < 0 or k == 0:
            return False
        # The trick is to group integers into buckets (i.e choose a hash function)
        # such that if two integers x and y are t distance apart, they are
        # guaranteed to be in neigbouring buckets. 
        # ex. t = 5, list = [2, 8, 20, 6], we'll use bucket = index / t
        # 2 -> bucket = 0, 8 -> bucket = 1, 20 -> bucket = 4, 6 -> bucket = 1
        # (2, 6) are in neighbouring buckets and (8, 6) are in the same bucket
        # We need to check three buckets but this is way better than checking the entire range of t
        buckets = {}
        for i, num in enumerate(nums):
            bucket = int(num/(t+1)) # using t+1 fixes the t = 0 case
            if bucket in buckets:
                return True
            if bucket-1 in buckets and abs(buckets[bucket-1]-num) <= t:
                return True
            if bucket+1 in buckets and abs(buckets[bucket+1]-num) <= t:
                return True
            # Remove the bucket of the i-k element, this guarantees
            # we're only keeping buckets with integers k distance apart
            if i-k >= 0:
                oldBucket = int(nums[i-k]/(t+1))
                if oldBucket in buckets:
                    del buckets[oldBucket]
            buckets[bucket] = num
        return False
    