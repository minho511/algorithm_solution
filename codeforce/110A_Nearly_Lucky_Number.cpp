#include <bits/stdc++.h>

using namespace std;


void solve(){
    string s, t;
    int cnt = 0;
    bool ans = 1;
    cin >> s;
    for(int i = 0; i<s.length(); i++){
        auto c = s.substr(i, 1);
        if((stoi(c)==4||stoi(c)==7)){
            cnt++;
        }
    }
    
    if(cnt==4||cnt==7) cout << "YES";
    else cout << "NO";
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}