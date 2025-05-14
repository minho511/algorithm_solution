#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    string a;
    char b;
    int cnt = 0;
    cin >> n;
    cin >> a;
    b = a[1];
    for(int i = 0; i< n-1; i++){
        cin >> a;
        if(a[0]==b) cnt++;
        b = a[1];
    }
    cout << cnt+1;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}