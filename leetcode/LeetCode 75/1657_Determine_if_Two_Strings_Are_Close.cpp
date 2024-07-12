class Solution {
public:
    bool closeStrings(string word1, string word2) {
        set<char> s1(word1.begin(), word1.end());
        set<char> s2(word2.begin(), word2.end());
        vector<int> c1, c2;
        if(s1!=s2) return false;
        else{
            for(auto c : s1){
                c1.push_back(count(word1.begin(), word1.end(), c));
                c2.push_back(count(word2.begin(), word2.end(), c));
            }
            sort(c1.begin(), c1.end());
            sort(c2.begin(), c2.end());
            return c1==c2;
        }
    }
};