# Solution 1: Use a heap to keep track of the minimum element in each list

# Runtime O(n*log(k)) where n is the total number of elements
# and k is the number of lists. This is because for every element we need
# to push/pop it from the heap once, and the heap is of size k.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        heap = []
        for i in range(len(lists)):
            if lists[i] is None:
                continue
            heap.append((lists[i].val,lists[i]))
        if len(heap) == 0:
            return None
        heapq.heapify(heap)
        front = heapq.heappop(heap)
        head = front[1]
        node = head
        if node.next is not None:
             heapq.heappush(heap, (node.next.val,node.next))
        while len(heap) > 0:
            front = heapq.heappop(heap)
            node.next = front[1]
            if node.next.next is not None:
                heapq.heappush(heap, (node.next.next.val,node.next.next))
            node = node.next
        return head
    
    