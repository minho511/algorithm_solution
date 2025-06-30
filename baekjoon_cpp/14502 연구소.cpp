#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, m, x, y;
const int MaxN = 8;
const int MaxM = 8;
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};
int g[MaxN][MaxM];
bool visited[MaxN][MaxM];
queue<pair<int, int>> q;

// 0: 빈칸 | 1 : 벽 | 2 : 바이러스
void dfs(int x, int y){
    visited[x][y] = 1;
    for(int i = 0; i<4; i++){
        int nx = dx[i] + x;
        int ny = dy[i] + y;
        if(nx < 0 || ny < 0 || nx>=n || ny>=m) continue;
        if(visited[nx][ny] == 1) continue;
        if(g[nx][ny] == 1) continue;
        dfs(nx, ny);
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int MaxSafe = 0;

    cin >> n >> m;
    for(int i = 0; i< n; i++){
        for(int j = 0; j< m; j++)
            cin >> g[i][j];
    }    
    
    vector<pair<int, int>> candi;
    vector<pair<int, int>> virus;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(g[i][j] == 0) candi.push_back({i, j});
            else if(g[i][j] == 2) virus.push_back({i, j});
        }
    }
    for(int i = 0; i < candi.size()-2; i++){
        for(int j = i+1; j< candi.size()-1; j++){
            for(int k = j+1; k< candi.size(); k++){
                memset(visited, false, sizeof(visited));        
                tie(x, y) = candi[i];
                g[x][y] = 1;
                tie(x, y) = candi[j];
                g[x][y] = 1;
                tie(x, y) = candi[k];
                g[x][y] = 1;
                int safeRegion = 0;
                for(auto c : virus){
                    tie(x, y) = c;
                    dfs(x, y);        
                }
                for(int p = 0; p< n; p++){
                    for(int q = 0; q< m; q++){
                        if(g[p][q] == 0 && visited[p][q] == 0) safeRegion++;
                    }
                }
                tie(x, y) = candi[i];
                g[x][y] = 0;
                tie(x, y) = candi[j];
                g[x][y] = 0;
                tie(x, y) = candi[k];
                g[x][y] = 0;

                MaxSafe = max(safeRegion, MaxSafe);
            }
        }
    }

    cout << MaxSafe;
    return 0;
}