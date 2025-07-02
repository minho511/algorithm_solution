#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MaxN = 50;
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};
int g[MaxN][MaxN] = {0, };
bool visited[MaxN][MaxN] = {false,};
int L, R, x, y, cnt;
int n;
bool check;

void bfs(int a, int b){
    queue<pair<int, int>> q;
    vector<pair<int, int>> v;
    cnt = 0;
    int _sum = 0;
    q.push({a, b});
    while(q.size()){
        tie(x, y) = q.front(); q.pop();
        v.push_back({x, y});
        cnt++;
        _sum+=g[x][y];
        visited[x][y] = true;
        for(int i = 0; i< 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx<0 || ny<0 || nx>=n || ny>=n) continue;
            if(visited[nx][ny]) continue;
            int t = abs(g[x][y]-g[nx][ny]);
            if(L<=t && t<=R){
                visited[nx][ny] = true;
                q.push({nx, ny});
                check =true;
            }
        }
    }
    for(auto c: v){
        tie(x, y) = c;
        g[x][y] = _sum/cnt;
    }
    return;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n >> L >> R;
    for(int i = 0; i< n; i++){
        for(int j = 0; j< n; j++){
            cin >> g[i][j];
        }
    }
    check=true;
    int k = 0;
    while(check){

        check = false;
        for(int i = 0; i< n; i++){
            for(int j = 0; j< n; j++){
                if(visited[i][j]) continue;
                bfs(i, j);
            }
        }
        if(check) k++;
        memset(visited, false, sizeof(visited));
    }
    cout << k ;
    return 0;
}