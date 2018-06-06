# Solution 1: It is sufficient to just do a lookup to see if we 
# have already made an existing subset. Runtime = O(nlogn * (2^n))

# You may see the sort in the loop and say it's O(nlogn * (2^n)), which
# isn't wrong, but note that there is actually only one subset of length n.
# There are exponentially more subsets of length 1 (2^n / 2) or length 2 (2^n / 4), etc,
# so our sort is actually going to take much less than O(nlogn) on average. That's
# why this solution will still AC on LeetCode.
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        pset = []
        size = 2 ** len(nums)
        lookup = set()
        for i in range(size):
            subset = []
            for j in range(len(nums)):
                if (2**j) & i == (2**j):
                    subset.append(nums[j])
            subset.sort()
            if tuple(subset) not in lookup:
                pset.append(subset)
                lookup.add(tuple(subset))
        return pset

# Solution 2: We can still make our solution faster if we take the
# sort outside of the loop. In order to do this we need to observe that
# we can treat duplicates as special numbers.

# ex. if an element is duplicated 3 times, we add this element 0 -> 3 times to
# every existing subset in our list

# I went hard on this solution using list comprehension, but for some reason
# it only works with Python 3 on LeetCode
# Runtime = O(n * (2^n))
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        pset = [[]]
        i = 0
        while i < len(nums):
            num = nums[i]
            dupes = 1 # number of duplicates
            curr = i+1
            while curr < len(nums) and nums[curr] == nums[curr-1]:
                dupes += 1
                curr += 1
            # Add the num 0 -> dupes times to each subset
            for k in range(len(pset)):
                for j in range(1, dupes+1):
                    pset += [pset[k] + [num for k in range(j)]]
            i += dupes
        return pset

