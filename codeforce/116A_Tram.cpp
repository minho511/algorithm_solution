#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    int a, b;
    int t = 0;
    int M = 0;
    cin >> n;
    for(int i = 0; i<n;i++){
        cin >> a >> b;
        t = t-a+b;
        if(M< t){
            M = t;
        }
    }
    cout << M;

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}