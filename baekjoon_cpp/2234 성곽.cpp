#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MaxN = 51;
int n, m;
int g[MaxN][MaxN] = {0,};
int adj[MaxN*MaxN] = {0,};
int visited[MaxN][MaxN] = {0,};
int regionNum[MaxN][MaxN] = {0,};
int match[] = {2, 3, 0, 1};
int dx[] = {0, -1, 0, 1};
int dy[] = {-1, 0, 1, 0};
int maxR = 0;
int numR = 0;
int ans = 0;
queue<pair<int, int>> q;

void print(int b[][MaxN]){
    cout << "================" << endl;
    for(int i =0; i< m; i++){
        for(int j = 0; j< n; j++) cout << b[i][j] << ' ';
        cout << endl;
    }
    cout << '\n';
    cout << "================" << endl;
}

int bfs(int x, int y, int region, int mode){
    int cnt = 0;
    q.push({x, y});
    visited[x][y] = 1;
    while(q.size()){
        tie(x, y) = q.front(); q.pop();
        regionNum[x][y] = region;
        cnt++;
        for(int i = 0; i< 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx<0 || ny <0 || nx>=m ||ny>=n) continue;
            if(mode && regionNum[nx][ny]!=regionNum[x][y]){
                ans = max(ans, adj[region]+adj[regionNum[nx][ny]]);
            }
            if(g[x][y]&(1<<i)) continue;
            if(g[nx][ny]&(1<<match[i])) continue;
            
            if(visited[nx][ny]) continue;
            visited[nx][ny] = 1;
            q.push({nx, ny});
        }
    }
    return cnt;
}  

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;
    for(int i  = 0; i< m; i++){
        for(int j =0; j< n; j++){
            cin >> g[i][j];
        }
    }
    for(int i = 0; i< m; i++){
        for(int j= 0; j< n; j++){ 
            if(visited[i][j]) continue;
            numR++;
            adj[numR] = bfs(i, j, numR, 0);
            maxR = max(maxR, adj[numR]);
        }
    }
    cout << numR << endl;
    cout << maxR << endl;

    numR = 0;
    memset(visited, 0, sizeof(visited));
    for(int i = 0; i< m; i++){
        for(int j= 0; j< n; j++){ 
            if(visited[i][j]) continue;
            numR++;
            bfs(i, j, numR, 1);
        }
    }
    cout << ans << endl;
    return 0;
}