#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    int ans;
    cin >>n;
    if(n%2==0) ans = n/2;
    else ans = n*2*(-1)-1;
    cout << ans;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}