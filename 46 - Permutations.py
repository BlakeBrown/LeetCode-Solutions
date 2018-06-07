# Solution 1: Recursive solution by swapping
# Ex. [1,2,3]
# We should make the following recursive calls
# [1] + perm(2,3)
# [2] + perm(1,3)
# [3] + perm(1,2)

# Runtime: O(n*n!)
class Solution(object):
    def recursivePermute(self, nums, perms, perm):
        if len(nums) == 0:
            perms.append(perm)
            return
        for i in range(0,len(nums)):
            tmp = nums[0]
            nums[0] = nums[i]
            nums[i] = tmp
            self.recursivePermute(nums[1:],perms,perm + [nums[0]])
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = []
        self.recursivePermute(nums,perms,[])
        return perms

# Solution 2: Iterative solution using list concatentation, add 
# an element to every possible position in every existing permutation.
# Runtime: O(n*n!) since there are n! permutations and it takes O(n) time to build each one
# This runs slightly faster than the recursive solution due to less overhead.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Start with a permutation of just 1 element
        perms = [[nums[0]]]
        # For every remaining element, add it to every existing permutation in every possible index
        # ex. [1,2,3]
        # perms = [1]
        # Add 2 to [1] in every possible index (before and after)
        # perms = [2,1], [1,2]
        # Add 3 to [2,1] and [1,2] in every possible index
        # perms = [3,2,1], [2,3,1], [2,1,3], [3,1,2], [1,3,2], [1,2,3]
        for i in range(1,len(nums)):
            num = nums[i]
            for j in range(len(perms)):
                perm = perms[j]
                for k in range(len(perm)):
                    perms += [perm[0:k] + [num] + perm[k:]]
                perm.append(num) # add it to the end of the existing perm
        return perms

# Solution 3: Slightly more concise version of #2
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]]
        for num in nums:
            newPerms = []
            for perm in perms:
                for k in range(len(perm)+1):
                    newPerms.append(perm[0:k] + [num] + perm[k:])
            perms = newPerms
        return perms