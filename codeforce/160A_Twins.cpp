#include <bits/stdc++.h>
using namespace std;

bool comp(const int& a, const int& b) {return a>b;};

void solve(){
    int n, c, k, k2 = 0;
    int i = 0;
    cin >>n;
    vector<int> coin;
    for(int i=0; i< n;i++){
        cin >> c;
        coin.push_back(c);
    }
    sort(coin.begin(), coin.end(), comp);
    
    for(i = 0; i< n+1; i++){
        k = accumulate(coin.begin(), coin.begin()+i, 0);
        k2 = accumulate(coin.end()-(n-i), coin.end(), 0);
        if(k>k2){
            break;
        }
    }
    cout << i;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}