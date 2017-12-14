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
    vector<int> largestValues(TreeNode* root) {
        vector<int> solution;
        helper(solution, root, 0);
        return solution;
    }
    void helper(vector<int>&solution, TreeNode* root,int index) {
        if(root == NULL) {
            return;
        }
        if(solution.size() < index + 1) {
            solution.push_back(root->val);
        }
        else {
            if(solution[index] < root->val) {
                solution[index] = root->val;
            }
        }
        helper(solution, root->left, index + 1);
        helper(solution, root->right, index + 1);
    }
};
