class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
    
        int n = cost.size();
        int s1 = cost[0];
        int s2 = cost[1];
        int s3;
        for(int i = 2; i<n; i++){
            s3 = min(s1, s2)+cost[i];
            s1 = s2;
            s2 = s3;
        }
        return min(s1, s2);
    }
};