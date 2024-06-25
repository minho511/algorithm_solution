#include <bits/stdc++.h>
using namespace std;

void solve(){
    string a, b;
    cin >> a  >> b;
    bool ans = 1;
    auto l = a.length();
    for(int i = 0; i<l; i++){
        if(a[i]!=b[l-1-i]) ans = 0;
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