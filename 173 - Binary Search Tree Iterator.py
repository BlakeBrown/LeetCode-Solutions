# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        if root is not None:
            self.stack.append(root)
            while root.left is not None:
                root = root.left
                self.stack.append(root)
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        if node.right is not None:
            # Append right subtree
            root = node.right
            self.stack.append(root)
            # Append all nodes to the left
            while root.left is not None:
                root = root.left
                self.stack.append(root)
        return node.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())