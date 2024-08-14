class Solution {
public:
    int singleNumber(vector<int>& nums) {
        vector<bool> cnt(60001);
        for(auto x : nums){
            if(cnt[x+30000] == 1) cnt[x+30000] = 0;
            else cnt[x+30000] = 1;
        }
        auto idx = find(cnt.begin(), cnt.end(), 1);
        return idx-cnt.begin()-30000;
    }
};