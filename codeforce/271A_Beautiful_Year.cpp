#include <bits/stdc++.h>
using namespace std;


void solve(){
    string y;
    int i;
    cin >> y;
    vector<int> arr(10);
    i = stoi(y);
    i++;
    bool check = 1;
    y = to_string(i);
    while(1){
        check = 1;
        if(y == "2015") return;
        arr = {0, 0, 0, 0, 0,0, 0, 0, 0,0};
        for(int k = 0; k<4; k++){
            arr[stoi(y.substr(k, 1))]++;
        }
        for(int k = 0; k<10; k++){
            if(arr[k] >= 2){
                check = 0;
                break;
            }
        }
        
        if(check) break;
        i = stoi(y);
        i++;
        y = to_string(i);
    }
    cout << y;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}