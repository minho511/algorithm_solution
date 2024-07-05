class Solution {
public:
    bool isSubsequence(string s, string t) {
        int idx = 0;

        for(int i = 0; i<t.length(); i++){
            if(t[i]==s[idx]){
                idx++;
                if(idx==s.length()) 
                    return true;
            }
        }
        if(s=="")
            return true;
        return false;
    }
};