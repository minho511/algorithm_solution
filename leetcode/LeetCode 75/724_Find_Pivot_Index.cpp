class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        int sum = 0;
        int l=0, r=0;
        int ans = -1;
        for(int i = 0; i<n; i++){
            sum += nums[i];
            nums[i] = sum;
        }
        // i = 0
        if(nums[n-1] == nums[0]) return 0;

        for(int i = 1; i<n; i++){
            l = nums[i];
            r = nums[n-1]-nums[i-1];
            if(l==r){
                ans = i;
                break;
            }
        }
        return ans;

    }
};