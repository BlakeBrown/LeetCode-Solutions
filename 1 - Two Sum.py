from collections import defaultdict
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsDict = defaultdict(list)
        for index, element in enumerate(nums):
            numsDict[element].append(index)
        for i in numsDict:
            if target-i in numsDict:
                if target-i != i:
                    return [numsDict[target-i][0],numsDict[i][0]]
                elif len(numsDict[target-i]) > 1:
                    return numsDict[target-i]
