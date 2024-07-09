/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void dfs(TreeNode* node, int d, int* depth){
        if(node->left == NULL) *depth = max(*depth, d+1);
        else dfs(node->left, d+1, depth);
        if(node->right == NULL) *depth = max(*depth, d+1);
        else dfs(node->right, d+1, depth);
    }
    int maxDepth(TreeNode* root) {
        int depth = 0;
        if(root==NULL) return depth;
        dfs(root, 0, &depth);
        return depth;
    }
};