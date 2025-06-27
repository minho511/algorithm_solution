#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MaxN = 100;
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};

int n, x, y, k, t;

void dfs(int y, int x, int g[][MaxN], bool visited[][MaxN], int d){
    visited[y][x] = true;
    for(int i = 0; i< 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
        if(g[ny][nx] > d && !visited[ny][nx]) dfs(ny, nx, g, visited, d);
    }
}

void sol(){
    
    int ans = 0;
    int m = 0;
    int g[MaxN][MaxN] = {0,};
    cin >> n;
    for(int i = 0; i< n; i++){
        for(int j = 0; j<n; j++){
            cin >> g[i][j];
            m = max(g[i][j], m);
        }
    }


    for(int d = 0; d<m; d++){
        k = 0;
        bool visited[MaxN][MaxN] = {false,};
        for(int i = 0; i< n; i++){
            for(int j = 0; j< n; j++){
                if(g[i][j] > d && !visited[i][j]){
                        dfs(i, j, g, visited, d);
                        k++;                
                }
            }
        }
        ans = max(ans, k);
    }

    cout << ans;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    sol();
    return 0;
}