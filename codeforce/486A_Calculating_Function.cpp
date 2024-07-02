#include <bits/stdc++.h>
#define ll long long

using namespace std;

void solve(){
    ll n;
    ll ans;
    cin >>n;
    if(n%2==0) ans = n/2;
    else ans = -(n+1)/2;
    cout << ans;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}