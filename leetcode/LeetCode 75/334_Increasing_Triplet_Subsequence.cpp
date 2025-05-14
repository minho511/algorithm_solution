class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int n = nums.size();
        vector<int> m;
        vector<int> M;
        int nm = pow(2, 31)-1;
        int nM = -pow(2, 31);
        int i = 0;
        int j = n-1;
        
        while(i<=n-1){
            if(nums[i]< nm) nm = nums[i];
            if(nums[j]> nM) nM = nums[j];
            m.push_back(nm);
            M.push_back(nM);    
            i++;
            j--;
        }
        for(int i = 0; i<n; i++){
            if(m[i]<nums[i]&&nums[i]<M[n-1-i]) return true;
        }
        return false;

    }
};

// sol
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int n = nums.size();
        int fm = INT_MAX;
        int sm = INT_MAX;

        for(auto x : nums){
            if(x<fm) fm = x;
            else if(x>fm && x<sm) sm = x;
            else if(x>fm && x>sm) return true;
        }


        return false;

    }
};