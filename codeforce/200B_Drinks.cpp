#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n = 0;
    double a;
    double ans;
    cin >> n;
    for(int i = 0; i<n; i++){
        cin >> a;
        ans += a;
    }
    printf("%.10f",ans/(float)n);
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}