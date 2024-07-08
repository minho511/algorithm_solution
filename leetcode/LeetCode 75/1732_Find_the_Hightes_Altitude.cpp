class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int s = gain.size();
        int ans = 0;
        int k = 0;
        for(int i = 0; i<s; i++){
            k+=gain[i];
            ans = max(ans, k);
        }
        return ans;
    }
};