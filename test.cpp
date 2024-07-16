#include <bits/stdc++.h>

using namespace std;

int main(){
    vector<vector<int>> a;
    vector<int> b(4);
    for(int i = 0; i<4; i++){
        a.push_back(b);
    }
    for(int i = 0; i< 4; i++){
        for(int j = 0; j< 4; j++){
            cout << a[i][j];
        }
    }
    return 0;
}