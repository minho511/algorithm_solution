#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, p, q;
    int ans = 0;
    cin >> n;
    for(int i = 0; i<n;i++){
        cin >> p >> q;
        if((q-p)>=2) ans++;
    }
    cout << ans;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}