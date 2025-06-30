#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, m, x, y;
const int MaxN = 100;
const int MaxM = 100;
string g[MaxN];
int visited[MaxN][MaxM] = {0,};
queue<pair<int, int>> q;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;
    
    memset(visited, -1, sizeof(visited));
    
    for(int i = 0; i< n; i++){
        cin >> g[i];
        for(int j = 0; j<m;j++){
            if(g[i][j] == 'c'){
                q.push({i, j});
                visited[i][j] = 0;
            }   
        }
    }
    
    while(q.size()){
        tie(x, y) = q.front(); q.pop();
        int nx = x;
        int ny = y+1;
        if(ny < 0 || ny>=m) continue;
        if(g[nx][ny] == 'c' || visited[nx][ny] > -1) continue;
        visited[nx][ny] = visited[x][y] + 1;
        q.push({nx, ny});
    }
    for(int i = 0; i< n; i++){
        for(int j = 0; j< m; j++){
            cout << visited[i][j] << ' ';
        }
        cout << '\n';
    }
    return 0;
}