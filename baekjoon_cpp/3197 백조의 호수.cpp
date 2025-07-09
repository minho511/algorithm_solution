#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};
string g[1501];
int r, c;
bool visited[1501][1501] = {0,};
int cnt[1501][1501] = {0,};;
string s;
int x1;
int Y1;
int x2;
int y2;

void bfs(int x, int y){
    queue<pair<int, int>> q;
    q.push({x, y});
    visited[x][y] = 1;
    bool check1 = false;
    bool check2 = false;
    while(q.size()){
        tie(x, y) = q.front(); q.pop();
        for(int i = 0; i< 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx < 0 || ny < 0 || nx >= r || ny >= c) continue;
            if(nx == x2 && ny == y2) return;
            if(visited[nx][ny]) continue;
            if(g[nx][ny] == 'X'){
                
            }
            visited[nx][ny] = 1;
            q.push({nx, ny});
        }
    }
    return;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> r >> c;
    x1 = -1;
    for(int i = 0; i< r; i++){
        cin >> s;
        g[i] = s;
        for(int j = 0; j < c; j++){
            if(g[i][j] == 'L' && x1== -1){
                x1 = i;
                Y1 = j;
            }else if(g[i][j] == 'L'){
                x2 = i;
                y2 = j;
            }
        }
    }

    bfs(x1, Y1);
    
    return 0;
}