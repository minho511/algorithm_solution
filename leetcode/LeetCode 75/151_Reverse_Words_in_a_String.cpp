class Solution {
public:
    string reverseWords(string s) {
        vector<string> words;
        string w;
        string ans = "";
        for(int i = 0; i< s.length(); i++){
            if((s[i]==' ') && (i!=0 && s[i-1]!=' ')){
                words.push_back(w);
                w = "";
            }
            
            if(s[i] != ' ') w+=s[i];

            if(i==s.length()-1 && w.compare("")!=0){
                words.push_back(w);
            }
        }
        for(int i = words.size()-1; i>=0; i--){
            ans += words[i];
            if(i!=0) ans += " ";
        }
        return ans;
    }
};