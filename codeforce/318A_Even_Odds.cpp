#include <bits/stdc++.h>
#define ll long long

using namespace std;

void solve(){
    ll n, k;
    ll ans;
    cin >> n >> k;
    if((n+1)/2<k){
        ans = (k-(n+1)/2)*2;
    }
    else{
        ans = k*2-1;
    }
    cout << ans;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}