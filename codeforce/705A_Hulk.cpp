#include <bits/stdc++.h>
#define ll long long

using namespace std;

void solve(){
    int n;
    cin >> n;
    cout << "I hate";
    for(int i = 2; i<= n; i++){
        if(i%2==0){
            cout << " that I love";
        }else{
            cout << " that I hate";
        }
    }
    cout << " it";
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}