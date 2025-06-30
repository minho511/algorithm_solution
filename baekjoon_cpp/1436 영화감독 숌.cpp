#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    int k = 666;
    // for(;;k++){
    //     if(to_string(k).find("666") != string::npos) n--;
    //     if(n==0) break;
    // }
    // cout << k;
    int cnt = 0;
    while(1){
        bool check = false;
        string sk = to_string(k);
        for(int i = 2; i<sk.size(); i++){
            if(sk[i-2] == '6' && sk[i-1] == '6' && sk[i] == '6'){
                check = true;
                break;
            }
        }
        if(check){
            cnt++;
            if(cnt == n) break;
            
        }
        k++;
    }
    cout << k;
    return 0;
}