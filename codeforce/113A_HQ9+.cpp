#include <bits/stdc++.h>
#define ll long long

using namespace std;

void solve(){
    string s;
    bool ans = 0; 
    string hq = "HQ9";

    cin >> s;
    for(int i = 0; i<4; i++){
        if(s.find(hq[i]) != string::npos){
            ans = 1;
            break;
        }
    }
    if(ans) cout << "YES";
    else cout << "NO";
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}