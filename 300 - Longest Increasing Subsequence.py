# Solution 1: An O(n^2) algorithm is to start from the back of the array.
# Observe that the last element creates an LIS of size 1. Move to the
# second last element and observe that this will either create
# an LIS of size 2 (if it is smaller than the last element), or a new LIS of size 1.
# Repeat this process.
# Move backwards through the array keeping track of <start of LIS, length of LIS>.
# Each element will either start a new LIS of size 1, or add to an existing LIS.

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) <= 1):
            return len(nums)
        lis = [] # list of <start of LIS, length of LIS>
        for i in range(len(nums)-1,-1,-1):
            lisLength = None
            # Check if there's an existing LIS we can add to
            for j in range(0, len(lis)):
                if nums[i] < lis[j][0]:
                    if lisLength is None:
                        lisLength = lis[j][1]
                    elif lis[j][1] > lisLength:
                        lisLength = lis[j][1]
            # Add to existing LIS, or start a new one
            if lisLength:
                lis.append([nums[i],lisLength+1])
            else:
                lis.append([nums[i], 1])
        maxLis = 1
        for i in range(0, len(lis)):
            if(lis[i][1] > maxLis):
                maxLis = lis[i][1]
        return maxLis


# Solution 2: Let's make a small optimization.
# Observe that we only need to store the LARGEST element that starts an LIS.
# Ex. Let's say our list is [1, 110, 100]
# 100 starts an LIS of length 1. When we get to 110, rather than adding a new LIS of length 1,
# we can just update our existing LIS to use 110 instead of 100. This is because
# every element that would create a longer LIS with 100 will also create a longer LIS
# with 110.

# We can see how this logic works with the following example.

# Ex. Our list is [1,3,6,7,9,4,10,5,6]
# <length of LIS, largest element that starts LIS>
# 1st iteration: <1,6>
# 2nd iteration: <1,6>,  <2,5>
# 3rd iteration: <1,10>, <2,5> *** UPDATE
# 4th iteration: <1,10>, <2,5>, <3,5>
# 5th iteration: <1,10>, <2,5>, <3,5>, <4, 4>
# 6th iteration: <1,10>, <2,9>, <3,5>, <4, 4> *** UPDATE
# 7th iteration: <1,10>, <2,9>, <3,6>, <4, 4> *** UPDATE
# 8th iteration: <1,10>, <2,9>, <3,6>, <4, 4>, <5, 3>
# 9th iteration: <1,10>, <2,9>, <3,6>, <4, 4>, <5, 3>, <6, 1>
# Longest LIS = length 6, starting with element 1

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) <= 1):
            return len(nums)
        lis = [] # list of <length of LIS, largest element that starts LIS>
        for i in range(len(nums)-1,-1,-1):
            update = 0
            for j in range(0, len(lis)):
                if nums[i] == lis[j][1]:
                    update = 1 # if there's a duplicate element, don't do anything
                    break
                if nums[i] > lis[j][1]:
                    lis[j][1] = nums[i]
                    update = 2
                    break
            if update == 0:
                lis.append([len(lis)+1, nums[i]])
        return len(lis)


# Solution #3: Notice that we don't actually need to store tuples anymore.
# We can just use the array index to represent the LIS length.

# I also noticed when writing this that we don't actually need to look
# from the back of the array :) Let's write the forloop from 0 -> n

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) <= 1):
            return len(nums)
        lis = [] # lis[i] = largest element that starts an LIS of length i
        for i in range(0,len(nums)):
            update = 0
            for j in range(0, len(lis)):
                if nums[i] == lis[j]:
                    update = 1 # if there's a duplicate LIS, don't do anything
                    break
                if nums[i] < lis[j]:
                    lis[j] = nums[i]
                    update = 2
                    break
            if update == 0:
                lis.append(nums[i])
        return len(lis)

# Solution #4: O(nlogn) solution. Notice the lis list is always sorted. So we can
# use a binary search to determine where to update instead of a linear search.

import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) <= 1):
            return len(nums)
        lis = [nums[0]] # lis[i] = largest element that starts an LIS of length i
        for i in range(1,len(nums)):
            binarySearchIndex = bisect.bisect(lis,nums[i])
            # Avoid duplicate LIS
            if binarySearchIndex > 0 and lis[binarySearchIndex-1] == nums[i]:
                continue
            if binarySearchIndex == len(lis):
                lis.append(nums[i])
            else:
                lis[binarySearchIndex] = nums[i]
        return len(lis)
