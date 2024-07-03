class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string ans = "";
        int l1 = word1.length();
        int l2 = word2.length();
        int idx1 = 0;
        int idx2 = 0;

        while(idx1<l1 || idx2<l2){
            if(idx1<l1){
                ans.push_back(word1[idx1]);
                idx1++;
            }
            if(idx2<l2){
                ans.push_back(word2[idx2]);
                idx2++;
            }
        }

        return ans;
    }
};