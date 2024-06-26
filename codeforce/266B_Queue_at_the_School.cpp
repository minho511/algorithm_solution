#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, t;
    string line;
    cin >> n >> t;
    cin >> line;
    for(int i =0; i< t; i++){
        for(int j=0; j<n-1; j++){
            if(line[j] == 'B' && line[j+1] == 'G'){
                line[j] = 'G';
                line[j+1] = 'B';
                j++;
            }
        }
    }
    cout << line;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}