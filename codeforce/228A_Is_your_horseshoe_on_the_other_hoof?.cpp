#include <bits/stdc++.h>
#define ll long long

using namespace std;

void solve(){
    int ans = 0;
    int s1, s2, s3, s4;
    set<int> s;
    cin >> s1 >> s2 >> s3 >> s4;
    s.insert(s1);
    s.insert(s2);
    s.insert(s3);
    s.insert(s4);
    cout << 4-s.size();
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}