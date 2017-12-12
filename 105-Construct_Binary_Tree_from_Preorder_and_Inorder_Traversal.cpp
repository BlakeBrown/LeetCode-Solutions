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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return tree(inorder, preorder, 0, 0, inorder.size(), preorder.size());
    }
public:
    TreeNode* tree(vector<int>& inorder, vector<int>& preorder,int lowi,int lowp,int highi,int highp) {
        for(int i = lowp; i < highp; i++){
            int index = findIndex(lowi, highi - 1, inorder, preorder[i]);
            if(index != -1){
                int rootdata = inorder[index];
                TreeNode *root;
                root = new TreeNode(rootdata);
                root->left = tree(inorder, preorder, lowi, i + 1, index, highp);
                root->right = tree(inorder, preorder, index + 1, i + 1, highi, highp);
                return root;
            }
        }
        return NULL;
    }
public:
    int findIndex(int low, int high, vector<int> &a, int val) {
        for(int i = low; i <= high; i++) {
            if(a[i] == val) {
                return i;
            }
        }
        return -1;
    }
};
