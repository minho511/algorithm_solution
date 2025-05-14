// sol1 함수 활용
class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        set<int> A(nums1.begin(), nums1.end());
        set<int> B(nums2.begin(), nums2.end());
        vector<int> diffA2B(A.size());
        vector<int> diffB2A(B.size());
        vector<vector<int>> ans;
        auto iter1 = set_difference(A.begin(), A.end(), B.begin(), B.end(), diffA2B.begin());
        auto iter2 = set_difference(B.begin(), B.end(), A.begin(), A.end(), diffB2A.begin());
        diffA2B.erase(iter1, diffA2B.end());
        diffB2A.erase(iter2, diffB2A.end());
        ans.push_back(diffA2B);
        ans.push_back(diffB2A);
        return ans;
    }
};

// sol2
class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        set<int> A(nums1.begin(), nums1.end());
        set<int> B(nums2.begin(), nums2.end());
        vector<vector<int>> ans;
        vector<int> va;
        vector<int> vb;
        
        for(auto x : A){
             if(B.count(x)==0) va.push_back(x);
        }
        sort(va.begin(), va.end());
        ans.push_back(va);

        for(auto x2 : B){
             if(A.count(x2)==0) vb.push_back(x2);
        }
        sort(vb.begin(), vb.end());
        ans.push_back(vb);
        
        return ans;
    }
};
