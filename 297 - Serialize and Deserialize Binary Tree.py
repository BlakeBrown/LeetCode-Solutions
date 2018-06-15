# Solution: Do an iterative level order traversal by using a queue.

# Alternatively you can do a recursive pre-order traversal.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized = deque([])
        queue = deque()
        if root is not None:
            queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            if node is None:
                serialized.append(None)
                continue
            queue.append(node.left)
            queue.append(node.right)
            serialized.append(node.val)
        return serialized

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return []
        root = TreeNode(data.popleft())
        queue = deque([root])
        while len(queue) > 0 and len(data) > 0:
            node = queue.popleft()
            left = data.popleft()
            right = data.popleft()
            if left is not None:
                node.left = TreeNode(left)
                queue.append(node.left)
            if right is not None:
                node.right = TreeNode(right)
                queue.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))