# Solution 1: O(n^2) solution with sorting to prevent dupes
# TLE's on inputs like [0,0,0,0,0,0,0,0,...]
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lookup = {}
        for i in range(len(nums)):
            lookup[nums[i]] = i
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                check = -1*(nums[i]+nums[j])
                if check in lookup and lookup[check] > j:
                    ans.add(tuple(sorted((nums[i],nums[j],check))))
            if i > 1 and nums[i] == nums[i-1]:
                continue
        return list(ans)

# Solution 2: Don't create dupes in the first place, sort the input first.
# Still TLE's on large inputs!
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        lookup = {}
        for i in range(len(nums)):
            lookup[nums[i]] = i
        ans = []
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                check = -1*(nums[i]+nums[j])
                if check in lookup and lookup[check] > j:
                    ans.append([nums[i],nums[j],check])
                # Don't test the same j twice
                while j+1 < len(nums) and nums[j] == nums[j+1]:
                    j += 1
                j += 1
            # Don't test the same i twice
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return ans

# Solution 3: Let's great rid of the hashtable and just use the fact that the
# array is sorted to generate our solutions.
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        i = 0
        while i < len(nums):
            # Don't test the same i twice
            while i > 0 and i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            l = i + 1 # left side of array
            r = len(nums)-1 # right side of array
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                elif s == 0:
                    ans.append([nums[i],nums[l],nums[r]])
                    l += 1
                    # don't use a working l twice
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
            i += 1
        return ans


