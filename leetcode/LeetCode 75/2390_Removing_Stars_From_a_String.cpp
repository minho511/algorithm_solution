class Solution {
public:
    string removeStars(string s) {
        string stack = "";
        int n = s.length();
        for(int i = 0; i<n; i++){
            if(s[i] == '*'){
                stack.pop_back();
            }else{
                stack.push_back(s[i]);
            }
        }
        

        return stack;
    }
};