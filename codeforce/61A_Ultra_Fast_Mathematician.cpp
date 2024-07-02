#include <bits/stdc++.h>
#define ll long long

using namespace std;

void solve(){
    string s1, s2;
    cin >> s1 >> s2;
    for(int i = 0; i< s1.length(); i++){
        if(s1[i]==s2[i]) cout << "0";
        else cout << "1";
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}