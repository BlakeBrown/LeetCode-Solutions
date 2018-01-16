/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool has_sum(int sum, TreeNode* root)
    {
        if(root->left !=NULL && root->right!=NULL)
            return (has_sum(sum-(root->val),root->left) || has_sum(sum-(root->val),root->right));
        else if(root->left!=NULL)
            return has_sum(sum-(root->val),root->left);
        else if(root->right!=NULL)
            return has_sum(sum-(root->val),root->right);
        else
        {
            sum-=(root->val);
            if(sum==0)
                return true;
            return false;
        }
    }
    bool hasPathSum(TreeNode* root, int sum) {
        if(root!=NULL)
            return has_sum(sum,root);
        return false;
    }
};
