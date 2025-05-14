class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        chars.push_back('A');
        int cnt = 1;
        char t = chars[0];
        int i = 1;
        int temp = 0;
        while(i<chars.size()){
            if(t!=chars[i]){
                t = chars[i];
                if(cnt>1){
                    chars.erase(chars.begin()+i-cnt+1, chars.begin()+i);
                    i = i-cnt+1;
                    temp = 0;
                    while(cnt>0){
                        chars.insert(chars.begin()+i, (cnt%10)+48);
                        cnt/=10;
                        temp++;
                    }
                    i += temp;
                }
                cnt =1;
            }else{
                cnt++;
            }
            i++;
        }
        chars.pop_back();
        return chars.size();
    }
};