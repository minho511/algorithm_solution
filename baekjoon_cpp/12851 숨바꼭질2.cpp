#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
queue<int> q;

int n, k;
int visited[100003] = {0,};
int cnt[100003] = {0,};
int pos1, pos2, pos3;
int next_pos(int x, int i){
    if(i == 0) return x-1;
    if(i == 1) return x+1;
    if(i == 2) return x*2;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> k;
    q.push(n);
    visited[n] = 1;
    cnt[n]++;
    while(q.size()){
        int x = q.front();q.pop();
        if(x == k){
            break;
        }
        for(int i = 0; i < 3;i++){
            int nx = next_pos(x, i);
            if(nx <0 || nx >100000) continue;
            if(visited[nx] == 0){
                cnt[nx]++;
                visited[nx] = visited[x]+1;
                q.push(nx);
            }else if(visited[nx] == visited[x]+1){
                cnt[nx]++;
                q.push(nx);
            }
        }
    }
    cout << visited[k]-1 << '\n';
    cout << cnt[k];
    return 0;
}