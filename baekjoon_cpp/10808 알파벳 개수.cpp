// https://www.acmicpc.net/problem/10808
#include <bits/stdc++.h>

using namespace std;

int main(){
    string s;
    vector<int> cnt(26);
    cin >> s;
    for(auto c : s) cnt[c-97]++;
    for(auto i : cnt) cout << i << ' ';
    
    return 0;
}