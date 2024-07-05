class Solution {
public:
    string reverseVowels(string s) {
        string vowels = "aeiouAEIOU";
        string ans = "";
        vector<char> temp;
        for(int i = 0; i< s.length(); i++){
            if(vowels.find(s[i])!=string::npos){
                temp.push_back(s[i]);
            }
        }
        for(int i = 0; i< s.length(); i++){
            if(vowels.find(s[i])!=string::npos){
                ans+=temp.back();
                temp.pop_back();
            }else{
                ans+=s[i];
            }
            
        }
        return ans;
    }

};