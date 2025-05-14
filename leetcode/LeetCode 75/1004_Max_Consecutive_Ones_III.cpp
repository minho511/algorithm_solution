//1308 ms 58.19 MB
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int cnt = 0;
        int n =nums.size();
        int M = 0;
        int p = 0;
        int k2 = k;
        for(int i = 0; i<n ; i++){
            if(nums[i] == 1){
                cnt++;
                M = max(M, cnt);
            }else{
                if(k2>0){
                    if(k == k2) p = i;
                    k2--;
                    cnt++;
                    M = max(M, cnt);
                }else{
                    if(k>0)
                        i = p;
                    cnt = 0;
                    k2 = k;
                    
                }
            }

        }
        return M;
    }
};