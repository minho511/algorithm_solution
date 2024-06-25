#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n,h;
    int a;
    int ans = 0;
    cin >> n >> h;
    for(int i = 0; i<n;i++){
        cin >> a;
        if(a<=h) ans++;
        else ans+=2;
    }
    cout << ans;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}