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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return tree(inorder, postorder, 0, 0, inorder.size(), postorder.size() );
    }
public:
    TreeNode* tree(vector<int>& inorder, vector<int>& postorder,int lowi,int lowp,int highi,int highp) {
        for(int i = highp - 1; i >= lowp ; i--){
            int index = findIndex(lowi, highi - 1, inorder, postorder[i]);
            if(index != -1){
                int rootdata = inorder[index];
                TreeNode *root;
                root = new TreeNode(rootdata);
                root->left = tree(inorder, postorder, lowi, lowp, index, highp - (highp - i) );
                root->right = tree(inorder, postorder, index + 1, lowp, highi, highp - (highp - i) );
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
