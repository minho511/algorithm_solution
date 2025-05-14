class Solution {
public:
    bool isVowels(char x){
        return x=='a'||x=='e'||x=='i'||x=='o'||x=='u';
    }

    int maxVowels(string s, int k) {
        int cnt = 0;
        int n = s.length();
        int M = 0;
        bool f;
        for(int i = 0; i<n; i++){
            if(i<k){
                f = isVowels(s[i]);
                cnt += f;
            }else{
                cnt = cnt + isVowels(s[i]) - isVowels(s[i-k]);
            }
            M = max(cnt, M);
        }
        return M;
    }
};