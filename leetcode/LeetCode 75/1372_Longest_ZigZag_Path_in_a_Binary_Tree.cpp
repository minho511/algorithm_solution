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
    // previous direction : right = 0 left = 1
    void dfs(TreeNode* node, bool direction,int zigzag, int* M){
        if(node == nullptr){
            *M = max(*M, zigzag-1);
            return;
        }
        if(direction == -1){
            dfs(node->right, 0, 1, M);
            dfs(node->left, 1, 1, M);
        } // root
        if(direction == 0){// previous direction right
            dfs(node->right, 0, 1, M);
            dfs(node->left, 1, zigzag+1, M);
        }
        if(direction == 1){//previous direction left
            dfs(node->right, 0, zigzag+1, M);
            dfs(node->left, 1, 1, M);
        }
        return;
    }

    int longestZigZag(TreeNode* root) {
        int ans = 0;
        dfs(root, -1, 0, &ans);
        return ans;
    }
};