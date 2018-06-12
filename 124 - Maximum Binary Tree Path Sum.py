# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = float('-inf')
        
    def maxPathSumHelper(self,node):
        if node is None:
            return 0
        # Check each individual node
        self.ans = max(self.ans, node.val) 
        # Leaves just return their values
        if node.left is None and node.right is None:
            return node.val
        left = max(0,self.maxPathSumHelper(node.left))
        right = max(0,self.maxPathSumHelper(node.right))
        # Check path rooted at node
        self.ans = max(self.ans,node.val+left+right)
        # Return the max of left path, right path
        return max(node.val+left,node.val+right)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPathSumHelper(root)
        return self.ans

       