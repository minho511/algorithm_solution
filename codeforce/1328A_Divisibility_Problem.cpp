#include <bits/stdc++.h>
#define ll long long

using namespace std;

int t;
int a, b, ans;

void solve(){
    cin >> t;

    for(int i=0; i<t; i++){
        cin >> a >> b;
        if(a%b==0) ans = 0;
        else ans = b*((a/b)+1)-a;
        
        cout << ans << '\n';
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}