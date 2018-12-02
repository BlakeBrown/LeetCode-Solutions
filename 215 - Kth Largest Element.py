# Solution 1: Use a heap, pretty straight forward
# Runtime: O(n + klogn) since it takes O(n) time to build the heap and O(klogn) to pop k times
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        for i in range(len(nums)-k):
            heapq.heappop(nums)
        return nums[0]

# Solution 2: Use quick select algorithm, this is pretty tricky!
# I recommend studying up on a partitioning scheme first. A few
# common ones are:
# - Lomuto
# - Hoare's
# - Dutch National Flag -> I'm using this one since we already used it in #75 - Sort Colors

# Runtime: Average case O(n), worst case O(n^2) but this is unlikely since we're choosing
# a random pivot each time
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        random.seed()
        return self.quickSelect(nums, 0, len(nums)-1, len(nums)-k)

    def quickSelect(self, nums, left, right, k):
        pivotIndex = random.randint(left, right)
        pivotIndex = self.partition(nums, left, right, pivotIndex)
        if pivotIndex == k:
            return nums[pivotIndex]
        elif pivotIndex < k: 
            return self.quickSelect(nums, pivotIndex+1, right, k)
        else:
            return self.quickSelect(nums, left, pivotIndex-1, k)
        
    # Let's use DNF (dutch national flag) algorithm for the partition
    def partition(self, nums, left, right, pivotIndex):
        pivot = nums[pivotIndex]
        i = left
        j = left
        k = right
        while j <= k:
            if nums[j] < pivot:
                self.swap(nums, i, j)
                i += 1
                j += 1
            elif nums[j] > pivot:
                self.swap(nums, j, k)
                k -= 1
            else:
                j += 1
        return k # k is the final location of the pivot

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp