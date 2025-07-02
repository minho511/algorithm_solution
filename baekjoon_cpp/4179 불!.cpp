#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MaxN = 1000;
const int MaxM = 1000;
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};
string g[MaxN];
string s;
int visited[MaxN][MaxM] = {0, };
int fvisited[MaxN][MaxM] = {0, };
int n, m, t,d, x, y;
queue<pair<int, int>> q;
queue<pair<int, int>> fq;

void fire_bfs(){
    while(fq.size()){
        tie(x, y) = fq.front(); fq.pop();
        for(int i = 0; i< 4; i++){
            int nx = dx[i] + x;
            int ny = dy[i] + y;
            if(nx <0 || nx>=n || ny <0 || ny>=m) continue;
            if(fvisited[nx][ny] > 0) continue;
            if(g[nx][ny] == 'F' || g[nx][ny] == '#') continue;
            fq.push({nx, ny});
            fvisited[nx][ny] = fvisited[x][y] +1;
        }
    }
}

void bfs(){
    
    while(q.size()){
        tie(x, y) = q.front(); q.pop();
        for(int i = 0; i< 4; i++){
            int nx = dx[i] + x;
            int ny = dy[i] + y;
            if(nx <0 || nx>=n || ny <0 || ny>=m){
                d = visited[x][y];
                return;
            }
            if(visited[nx][ny]>0) continue;
            if(g[nx][ny] == '#'||g[nx][ny] == 'F') continue;
            if(visited[x][y]+1>=fvisited[nx][ny]&&fvisited[nx][ny]) continue;
            q.push({nx, ny});
            visited[nx][ny] = visited[x][y]+1;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >> g[i];
        for(int j = 0; j< m; j++){
            if(g[i][j] == 'J'){
                q.push({i, j});
                visited[i][j] = 1;
            }else if(g[i][j] == 'F'){
                fq.push({i, j});
                fvisited[i][j] = 1;
            }
        }
    }

    d = -1;

    fire_bfs();
    
    bfs();
    
    if(d > -1) cout << d;
    else cout << "IMPOSSIBLE";

    return 0;
}