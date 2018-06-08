# Solution: The idea is that we can reverse the first half of the LinkedList, and then
# compare the first half with the second half to see if it's a palindrome.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        # Move through the list with fast and slow pointers,
        # when fast reaches the end, slow will be in the middle
        # Trick #1: At the same time we can also reverse the first half of the list
        tmp = slow.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = tmp
            tmp = slow.next
            slow.next = prev
        head.next = None
        # Trick #2: If fast is None, the string is even length
        evenCheck = (fast is None)
        if evenCheck:
            if slow.val != slow.next.val:
                return False
            slow = slow.next.next
        else:
            slow = slow.next
        # Check that the reversed first half matches the second half
        while slow is not None:
            if tmp is None or slow.val != tmp.val:
                return False
            slow = slow.next
            tmp = tmp.next
        return True
            
        