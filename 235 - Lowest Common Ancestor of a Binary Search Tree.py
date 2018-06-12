# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        elif p == root or q == root:
            return root
        elif p.val < root.val and q.val < root.val:
            # Both p and q in left subtree
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val > root.val and q.val > root.val:
            # Both p and q are in right subtree
            return self.lowestCommonAncestor(root.right,p,q)
        # Otherwise they're in different subtrees, we've found LCA
        return root
            
            