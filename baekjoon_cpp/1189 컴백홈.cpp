#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};
int r, c, k;
int hx, hy;
int ans = 0;
string g[6];

void dfs(int x, int y, bool visited[][6], int d){
    if(x == 0 && y == c-1){
        if(d == k) ans++;
        return;
    }
    for(int i = 0; i< 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx<0 || ny<0 || nx>=r || ny>=c) continue;
        if(g[nx][ny] == 'T'||visited[nx][ny]) continue;
        
        visited[nx][ny] = true;
        dfs(nx, ny, visited, d+1);
        visited[nx][ny] = false;
    }
    return;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> r >> c >> k;
    bool visited[6][6] = {false,};
    visited[r-1][0] = true;
    for(int i =0; i< r; i++)
        cin >> g[i];
    dfs(r-1, 0, visited, 1);
    cout << ans;
    return 0;
}