// https://www.acmicpc.net/problem/2979
#include <bits/stdc++.h>

using namespace std;

int main(){
    int A, B, C;
    int s, e;
    int tot = 0;
    cin >> A >> B >> C;
    vector<int> p(100);
    for(int i = 0; i< 3; i++){
        cin >> s >> e;
        for(int j = s; j<e; j++){
            p[j]++;
        }
    }
    for(int j = 0; j < 100; j++){
            if(p[j] == 1) tot+=A;
            if(p[j] == 2) tot+=B*2;
            if(p[j] == 3) tot+=C*3;
    }
    cout << tot;
    return 0;
}