#include <bits/stdc++.h>

using namespace std;
string s;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    getline(cin, s);

    for(auto c : s){
        if(97 <= c && c <= 122){
            if(c+13<=122) cout << (char)(c+13);
            else cout << (char)(c-13);
        }else if(65 <= c && c <= 90){
            if(c+13<=90) cout << (char)(c+13);
            else cout << (char)(c-13);
        }else{
            cout << c;
        }
    }

    return 0;
}