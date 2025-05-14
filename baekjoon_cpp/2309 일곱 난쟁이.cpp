// https://www.acmicpc.net/problem/2309
#include <bits/stdc++.h>

using namespace std;

int main(){
    vector<int> v(9);
    int sum(0), input; 
    for(int i = 0; i <9; i++){
        cin >> input;
        v[i] = input;
        sum += input;
    }
    sort(v.begin(), v.end());
    for(int i = 0; i < 8; i++){
        for(int j = i+1; j < 9; j++){
            if(sum - v[i] - v[j] == 100){
                for(int k = 0 ;k< 9; k++){
                    if(k==i | k==j) continue;
                    cout << v[k] << '\n';
                }
                return 0;
            }
        }
    }
    return 0;
}