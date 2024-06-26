#include <bits/stdc++.h>
using namespace std;

void solve(){
    vector<char> v = {'h', 'e', 'l', 'l', 'o'};
    int k = 0;
    string input;
    cin >> input;
    char c = v[0];
    for(int i = 0; i< input.length(); i++)
    {   
        if(input[i] == c){
            v.erase(v.begin());
            c = v[0];
        }
        if(v.size() == 0) break;
    }

    if(v.size()==0) cout << "YES";
    else cout << "NO";

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}