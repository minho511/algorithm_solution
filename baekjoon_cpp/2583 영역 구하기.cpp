#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MaxN = 100;
const int MaxM = 100;
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};

int n,m, x, y, k;
int a, b, c, d;
void dfs(int x, int y, int g[][MaxN], bool visited[][MaxN], int* cnt){
    visited[x][y] = true;
    (*cnt)++;
    for(int i = 0; i< 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
        if(g[nx][ny] == 0 && !visited[nx][ny]) dfs(nx, ny, g, visited, cnt);
    }
}

void sol(){
    
    int ans = 0;
    int cnt = 0;

    int g[MaxN][MaxM] = {0,};
    vector<int> area;
    bool visited[MaxN][MaxM] = {false,};
    cin >> m >> n >> k;
    for(int i = 0; i< k; i++){
        cin >> a >> b >> c >> d;
        for(int p = a; p < c; p++){
            for(int q = b; q < d; q++){
                g[p][q] = 1;
            }
        }
    }
    for(int i = 0; i< n; i++){
        for(int j = 0; j< m; j++){
            if(g[i][j]==0 && !visited[i][j]){
                ans++;
                cnt = 0;
                dfs(i, j, g, visited, &cnt);
                area.push_back(cnt);
            }
        }
    }
    cout << ans << '\n';
    sort(area.begin(), area.end());
    for(auto c : area)
    cout <<   c << ' ';
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    sol();
    return 0;
}