#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MaxN = 51;
const int MaxM = 51;
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};

int n, m, x, y, k, t;

void dfs(int y, int x, int g[][MaxM]){
    g[y][x] = 0;
    for(int i = 0; i< 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
        if(g[ny][nx] == 1) dfs(ny, nx, g);
    }
}

void sol(){
    
    int ans = 0;
    int g[MaxN][MaxM] = {0,};
    cin >> m >> n >> k;
    for(int i = 0; i< k; i++){
        cin >> x >> y;
        g[y][x] = 1;
    }
    for(int i = 0; i< n; i++){
        for(int j = 0; j< m; j++){
           if(g[i][j] == 1){
                dfs(i, j, g);
                ans++;
           }
        }
    }
    cout << ans << '\n';
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> t;
    for(int i =0; i< t; i++)
        sol();
    return 0;
}