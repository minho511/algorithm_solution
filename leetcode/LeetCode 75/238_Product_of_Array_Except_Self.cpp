class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int pro = 1;
        int n = nums.size();
        vector<int> ans(n);
        int zcnt = 0;
        for(auto x : nums){
            if(x==0) {
                zcnt++;
                continue;
            }
            pro*=x;
        }
        
        if(zcnt==1){
            for(int i = 0; i<n; i++){
                if(nums[i] == 0) ans[i] = pro;
                else ans[i] = 0;
            }
        }else if(zcnt==0){
            for(int i = 0; i<n; i++){
                ans[i] = pro/nums[i];
            }
        }
        return ans; //zcnt>1
    }
};