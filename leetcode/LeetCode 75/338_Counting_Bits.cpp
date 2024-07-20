class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> v = {0, 1, 1, 2, 1};
        vector<int> ans;
        // 0->0     0
        // 1->01    1
        // 2->10    1
        // 3->11    2 
        // 4->100   1
        // 5->101   2  1+1
        // 6->110   2  1+1
        // 7->111   3  2+1
        // 8->1000  1 
        // 9->1001  2  1+1
        // 10->1010 2  1+1
        // 11->1011 3  2+1
        // 12->1100 2  1+1
        // 13->1101 3  2+1
        // 14->1110 3  2+1
        // 15->1111 4  3+1
        // 16->10000 1
        if(n<5){
            ans = {v.begin(), v.begin()+n+1};
            return ans;
        }
        int k = (int)log2(n-1);
        for(int i = 1; i<k; i++){
            for(int j = 1; j<pow(2, i+1); j++){
                // i = 1    3  (1) 4-2-1
                // i = 2    5->7  (3) 8-4-1
                // i = 3    9->15  (7) 16-8-1
                v.push_back(v[j]+1);
            }
            v.push_back(1);
        }
        ans = {v.begin(), v.begin()+n+1};
        return ans;
    }
};