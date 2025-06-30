#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

string s = "0";
bool check1;
bool check2;
bool check3;
char pre;
int cntVowel;
int cntNoVowel;
bool isVowel(char c){
    if(c == 'a' || c =='e' || c=='i' || c=='o' || c=='u') return true;
    return false;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    while(1){
        cin >> s;
        if(s == "end") return 0;
        cntVowel = 0;
        cntNoVowel = 0;
        check1 = false;
        check2 = true;
        check3 = true;
        pre = s[0];
        for(int i = 0; i< s.size(); i++){
            if(isVowel(s[i])){
                check1 = true;
                cntVowel++;
                cntNoVowel = 0;
                if(cntVowel==3){
                    check2 = false;
                    break;
                }
            }else{
                cntNoVowel++;
                cntVowel = 0;
                if(cntNoVowel==3){
                    check2 = false;
                    break;
                } 
            }
            if(i>=1){
                if(pre == s[i] && pre != 'e' && pre != 'o'){
                    check3 = false;
                    break;
                }
                pre = s[i];
            }
        }
        if(check1&&check2&&check3)
            cout << "<" << s << "> " << "is" << " acceptable.\n";
        else
            cout << "<" << s << "> " << "is" << " not acceptable.\n";
    }
    return 0;
}