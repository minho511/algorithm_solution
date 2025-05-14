#include <bits/stdc++.h>
using namespace std;

void solve(){
    string a,b;
    
    int t;
    cin >> a;
    bool ans = 0;
    bool ans2 = 0;
    t = stoi(a);
    for(int i = 1; i<=t; i++){
        if(t%i != 0) continue;
        b = to_string(i);
        ans2 = 1;
        for(int j = 0; j<b.length(); j++){
            if(!(b[j]==52||b[j]==55)){
                ans2 = 0;
            }
        }
        if(ans2==1){
            ans = 1;
            break;
        }
    }

    if(ans == 0) cout << "NO";
    else cout << "YES";

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}