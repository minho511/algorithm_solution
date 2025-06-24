#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n;
    string s;
    bool c = false;
    cin >> n;
    
    vector<string> people(n); 
    vector<int> check(26);
    for(int i = 0; i< n; i++){
        cin >> s;
        check[s[0]-97]++;
    }
    for(int i =0; i< 26; i++){
        if(check[i]>=5){
            c = true;
            cout << char(i+97);
        }
    }
    if(!c) cout << "PREDAJA";
    return 0;
}