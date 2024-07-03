class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int max = *max_element(candies.begin(), candies.end());
        int n = candies.size();
        vector<bool> ans;
        for(int i = 0; i<n; i++){
            auto candy = candies[i];
            if(candy == max || candy+extraCandies >= max){
                ans.push_back(1);
                continue;
            }
            ans.push_back(0);
        }
        return ans;
    }
};