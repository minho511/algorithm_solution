#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int r, c;
string g[20];

const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};

int x, y;
int M = 1;

void dfs(int x, int y, int d, int visited[][20], bool Alpha[28]){
    for(int i = 0; i< 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx<0 || ny<0 || nx>=r || ny>=c) continue;
        if(visited[nx][ny]) continue;
        if(Alpha[g[nx][ny]-'A']) continue;
        visited[nx][ny] = 1;
        Alpha[g[nx][ny]-'A'] = 1;
        M = max(M, d+1);
        dfs(nx, ny, d+1, visited, Alpha);
        Alpha[g[nx][ny]-'A'] = 0;
        visited[nx][ny] = 0;
    }
    return;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int visited[20][20] = {0, };
    bool Alpha[28] = {0, };
    cin >> r >> c;
    for(int i = 0; i< r ; i++)
        cin >> g[i];
    visited[0][0] = 1;
    Alpha[g[0][0]-'A'] = 1;
    dfs(0, 0, 1, visited, Alpha);
    cout << M;
    return 0;
}