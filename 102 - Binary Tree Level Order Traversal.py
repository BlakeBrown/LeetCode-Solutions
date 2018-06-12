# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        count = 1
        newCount = 0
        queue = deque([root])
        ans = [[]]
        while len(queue) > 0:
            node = queue.popleft()
            ans[-1].append(node.val)
            if node.left is not None:
                queue.append(node.left)
                newCount += 1
            if node.right is not None:
                queue.append(node.right)
                newCount += 1
            if count > 0:
                count -= 1
            if count == 0:
                count = newCount
                newCount = 0
                ans.append([])
        ans.pop()
        return ans