#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

queue<int> q;
int visited[2][500001] = {0,};

int next_pos(int x, int i){
    if(i == 0) return x+1;
    if(i == 1) return x-1;
    if(i == 2) return x*2;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t = 1;
    int n, k;
    cin >> n >> k;
    if(n == k){cout << 0; return 0;}
    visited[0][n] = 1;
    q.push(n);
    while(q.size()){
        int size_q = q.size();
        k+=t;
        if(k > 500000){cout << -1; break;}
        if(visited[t%2][k]){cout << t; break;}
        for(int j = 0; j< size_q; j++){
            int x = q.front(); q.pop();
            for(int i = 0; i < 3; i++){
                int nx = next_pos(x,i);
                // cout << nx << ' ' << k << ' ' << t << endl;
                if(nx < 0 || nx > 500000) continue;
                if(visited[t%2][nx]) continue;
                if(nx == k){
                    cout << t << endl;
                    return 0;
                }
                visited[t%2][nx] = 1;
                q.push(nx);
            }
        }
        t++;
    }
    return 0;
}