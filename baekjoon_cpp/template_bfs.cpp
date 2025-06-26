#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, m, x, y;
const int MaxN = 100;
const int MaxM = 100;
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};
int g[MaxN][MaxM];
int visited[MaxN][MaxM];
queue<pair<int, int>> q;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;
    for(int i = 0; i< n; i++){
        for(int j = 0; j< m; j++)
            cin >> g[i][j];
    }
    q.push({0, 0});
    visited[0][0] = 1;
    while(q.size()){
        tie(x, y) = q.front(); q.pop();
        for(int i = 0; i< 4; i++){
            int nx = dx[i] + x;
            int ny = dy[i] + y;
            if(nx < 0 || ny < 0 || nx>=n || ny>=m) continue;
            if(g[nx][ny] == 0 || visited[nx][ny] > 0) continue;
            visited[nx][ny] = visited[x][y] + 1;
            q.push({nx, ny});
        }
    }
    cout << visited[n-1][m-1];
    return 0;
}