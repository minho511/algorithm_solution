#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MaxN = 50;
const int MaxM = 50;
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};
string g[MaxN];
int visited[MaxN][MaxM] = {0, };
int n, m;
int dist, ans;

void bfs(int x, int y){
    queue<pair<int, int>> q;
    q.push({x, y});
    while(q.size()){
        tie(x, y) = q.front(); q.pop();
        for(int i = 0; i< 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx < 0 || ny < 0 || nx>=n || ny>=m) continue;
            if(g[nx][ny] == 'W') continue;
            if(visited[nx][ny]>0 ) continue;
            visited[nx][ny] = visited[x][y]+1;
            dist = max(dist, visited[x][y]);
            q.push({nx, ny});
        }
    }
    return;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;
    for(int i = 0; i< n; i++){
        cin >> g[i];
    }    
    ans = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j< m; j++){
            if(g[i][j] == 'L'){
                visited[i][j] = 1;
                
                dist = 0;
                bfs(i, j);
                ans = max(dist, ans);
                memset(visited, 0, sizeof(visited));
            }
        }
    }
    cout <<ans;
    return 0;
}