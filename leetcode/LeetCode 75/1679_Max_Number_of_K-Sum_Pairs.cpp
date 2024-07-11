// 풀이 1 : 매우 비효율적 (758 ms)
class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int p;
        int start = 0;
        int end = n-1;
        int ans = 0;
        while(start<end){
            p = k-nums[start];
            if(nums[end]<p){
                start++;
            }else if(nums[end]==p){
                nums.erase(nums.begin()+start);
                nums.erase(nums.begin()+end-1);
                end-=2;
                ans++;
            }else{
                end--;
            }
        }
        return ans;
    }
};


// 풀이 2 (82 ms)
// erase 할 필요없이 포인터만 옮겨주면 됨.

class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int p;
        int start = 0;
        int end = n-1;
        int ans = 0;
        while(start<end){
            p = k-nums[start];
            if(nums[end]<p){
                start++;
            }else if(nums[end]==p){
                start++;
                end--;
                ans++;
            }else{
                end--;
            }
        }
        return ans;
    }
};



