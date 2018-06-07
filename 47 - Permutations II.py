# Solution 1: Use the recursive solution to Permutations I, and only
# add permutations we haven't made before
class Solution(object):
    def recursivePermute(self, nums, perms, perm):
        if len(nums) == 0:
            perms.add(tuple(perm))
            return
        for i in range(0,len(nums)):
            tmp = nums[0]
            nums[0] = nums[i]
            nums[i] = tmp
            self.recursivePermute(nums[1:],perms,perm + [nums[0]])
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = set()
        self.recursivePermute(nums,perms,[])
        permsList = []
        for perm in perms:
            permsList.append(list(perm))
        return permsList

# Solution 2: Use the iterative solution to Permutations I with a smart "trick"
# to eliminate duplicates. Note: This only works if you are creating permutations
# in the right order
class Solution(object):
    def permuteUnique(self, nums):
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
                    if k < len(perm) and perm[k] == num:
                        break
            perms = newPerms
        return perms