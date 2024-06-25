#include<iostream>
#include<algorithm>

using namespace std;

void solve(){
    string s;
    char a;
    bool check = 0;
    cin >> s;
    if(s.length()<7) cout << "NO";
    else{
        for(int i = 0; i<s.length()-6; i++){
            auto subs =  s.substr(i, 7);
            if(!subs.compare("1111111")||!subs.compare("0000000")){
                check=1;
                break;
            }
        }
        if(check) cout << "YES";
        else cout << "NO";
    }
    
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}