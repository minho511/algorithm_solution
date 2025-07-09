#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n, m, sx, sy, ex, ey, x, y;
string g[301];
bool check;
bool visited[301][301] = {0, };
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int cnt = 0;

bool bfs(int xx, int yy){
    queue<pair<int, int>> q;
    q.push({xx, yy});
    while(q.size()){
        tie(x, y) = q.front();q.pop();
        for(int i =0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx <0 || ny <0 || nx >= n || ny >=m) continue;
            if(visited[nx][ny]) continue;
            if(nx == ex && ny == ey){
                return true;
            }
            if(g[nx][ny] == '1'){
                visited[nx][ny] = 1;
                continue;
            }
            visited[nx][ny] = 1;
            q.push({nx, ny});
        }
    }
    for(int i = 0; i< n ;i++){
        for(int j = 0; j< m ; j++){
            if(g[i][j] == '1' && visited[i][j] == 1){
                g[i][j] = '0';
            }
            // cout << g[i][j] << ' ' ;
        }
        // cout << endl;
    }
    return false;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;
    cin >> sx >> sy >> ex >> ey;
    sx--;sy--;ex--;ey--;
    for(int i = 0; i< n; i++){
        cin >> g[i];
    }
    visited[sx][sy] = 1;
    do{
        memset(visited, 0, sizeof(visited));
        check = bfs(sx, sy);
        cnt++;
    }while(!check);
    cout << cnt;

    return 0;
}