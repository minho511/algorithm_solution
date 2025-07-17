#include <bits/stdc++.h>
using namespace std;
string s;

int main(){
    cin >> s;
    bool check = true;
    int n = s.size();
    for(int i = 0; i<n; i++){
        if(s[i] == 'p' && i<n-1 && s[i+1]=='i') i++;
        else if(s[i] == 'k' && i<n-1 && s[i+1] == 'a') i++;
        else if(s[i] == 'c' && i<n-2 && s[i+1] == 'h' && s[i+2] == 'u') i+=2;
        else {
            check = false;
            break;
        }
    }
    cout << (check ? "YES" : "NO");
}