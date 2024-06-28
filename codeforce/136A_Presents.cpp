#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, a;
    cin >>n;
    vector<int> v(n);
    for(int i = 1; i<=n; i++){
        cin >> a;
        v[a-1] = i;
    }
    for(int i =0; i<n; i++){
        cout << v[i] << ' ';
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}