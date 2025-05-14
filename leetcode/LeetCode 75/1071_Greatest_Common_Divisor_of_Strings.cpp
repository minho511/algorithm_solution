class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        int l1 = str1.length(), l2=str2.length();
        string t;
        bool check, check2 = 0;
        for(int i = l1; i>0; i--){
            check = 1;
            t = str1.substr(0, i);
            for(int j = i; j<l1; j+=i){
                if(t.compare(str1.substr(j, i))!=0){
                    check = 0;
                    break;
                }
            }
            if(check){
                check2 = 1;
                for(int j = 0; j<l2; j+=i){
                    if(t.compare(str2.substr(j, i))!=0){
                        check2 = 0;
                        break;
                    }
                }
                if(check2) break;
            }
        }
        if(check2) return t;
        else return "";
    }
};