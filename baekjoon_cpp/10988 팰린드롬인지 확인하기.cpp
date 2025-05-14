// https://www.acmicpc.net/problem/2979
#include <bits/stdc++.h>

using namespace std;

int main(){
    string s;
    cin >> s;
    bool res = 1;
    for(int i = 0; i< s.length()/2; i++){
        if(s[i] != s[s.length()-1-i]){
            res = 0;
            break;
        }
    }
    cout << res;
    return 0;
}