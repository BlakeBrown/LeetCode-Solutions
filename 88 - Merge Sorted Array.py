class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        newArr = [0] * len(nums1)
        ptr1 = 0
        ptr2 = 0
        for i in range(len(nums1)):
            if ptr1 >= m:
                newArr[i] = nums2[ptr2]
                ptr2 += 1
            elif ptr2 >= n:
                newArr[i] = nums1[ptr1]
                ptr1 += 1
            elif nums1[ptr1] < nums2[ptr2]:
                newArr[i] = nums1[ptr1]
                ptr1 += 1
            else:
                newArr[i] = nums2[ptr2]
                ptr2 += 1
        for i in range(len(newArr)):
            arr1[i] = newArr[i]