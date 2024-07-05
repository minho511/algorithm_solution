class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        cout.tie(nullptr);
        
        double ans = -10000, a;
        for(int i = 1; i<nums.size(); i++){
            nums[i] = nums[i-1] + nums[i];
        }
        for(int i = k-1; i<nums.size(); i++){
            if(i==k-1) a = nums[i];
            else{
                a = nums[i]-nums[i-k];
            }
            a/=k;
            if(a>ans) ans = a;
        }
        
        return ans;
    }
};