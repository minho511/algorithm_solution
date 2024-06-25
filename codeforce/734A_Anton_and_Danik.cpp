#include <bits/stdc++.h>
using namespace std;

void solve(){

    int n, a, d = 0;
    string s;
    cin >> n >> s;
    a = count(s.begin(), s.end(), 'A');
    d = n-a;

    if(a==d) cout << "Friendship";
    else if(a>d) cout << "Anton";
    else cout << "Danik";
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
}
