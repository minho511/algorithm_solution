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
    
    void dfs(TreeNode* curr, int val, TreeNode* ans, bool* find){
        
        if(curr->val == val){
            ans->val = curr->val;
            ans->left = curr->left;
            ans->right = curr->right;
            *find = true;
            return;
        }
        if(curr->right==NULL && curr->left==NULL) return;
        if(curr->right!=NULL) dfs(curr->right, val, ans, find);
        if(curr->left!=NULL) dfs(curr->left, val, ans, find);
        return;
    }

    TreeNode* searchBST(TreeNode* root, int val) {
        TreeNode* ans = new TreeNode();
        bool find = false;
        dfs(root, val, ans, &find);
        return find?ans:NULL;
    }
};


// 빠른 코드
Cpp
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
    TreeNode* solve(TreeNode* node, int val)
    {
        if(node==NULL)
        return NULL;
        
        if(node!=NULL and node->val==val)
        return node;

        if(val < node->val)   // BST 의 특성을 이용, val 이 node 보다 작다면 왼쪽을 탐색
        return solve(node->left,val);

        return solve(node->right,val);
    }

    TreeNode* searchBST(TreeNode* root, int val) 
    {
        return solve(root,val);    
    }
};