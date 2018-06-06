# Solution 1: Iterative O(n*(2^n))
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        pset = []
        size = 2 ** len(nums)
        for i in range(size):
            subset = []
            for j in range(len(nums)):
                if (2**j) & i == (2**j):
                    subset.append(nums[j])
            pset.append(subset)
        return pset

# Solution 2: Recursive O(n*(2^n))
class Solution(object):
    def pset(self, nums, subsets):
        if len(nums) == 0:
            return subsets
        newSubsets = []
        for i in range(len(subsets)):
            subset = subsets[i]
            newSubsets.append(subset)
            # HUGE gotcha on the next line
            # You can't use subset.append(nums[0]) because this will mutate subset!!
            # Instead use subset + [nums[0]] which gives a new list
            newSubsets.append(subset + [nums[0]])
        subsets = newSubsets
        return self.pset(nums[1:],subsets)
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        subsets.append([])
        subsets.append([nums[0]])
        return self.pset(nums[1:], subsets)

# Solution 3: I thought this solution was beautiful, takes advantage
# of list comprehension in Python.
# Runtime: O(n * (2^n)), it's hard to see with this concise code but keep in mind
# there are still 2^n subsets and it takes O(n) time to build each of them
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        pset = [[]] # we'll always have the empty set
        for num in nums:
            pset += [subset + [num] for subset in pset]
        return pset