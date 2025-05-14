class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        for(auto x: nums){
            if(x == val) continue;
            k++;
        }
        remove(nums.begin(), nums.end(), val);
        return k;
    }
};