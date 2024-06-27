#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    int a;
    cin >> n;
    bool ans = 0;
    while(n){
        cin >> a;
        if(a == 1){
            ans = 1;
            break;
        }
        n--;
    }
    if(ans) cout << "HARD";
    else cout << "EASY";
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}