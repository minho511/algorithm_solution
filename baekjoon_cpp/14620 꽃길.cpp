#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MaxN = 10;
int g[MaxN][MaxN] = {0,};
int dx[] = {0, -1, 1, 0, 0};
int dy[] = {0, 0, 0, 1, -1};
int n, x, y, temp, flag;
int ans = 20001;
int cnt = 0;


void dfs(int d, int cost, int visited[][MaxN]){
    if(d == 3){
       ans = min(ans, cost);
       return;
    }
    for(int i = 1 ;i< n-1; i++){
        for(int j = 1; j<n-1; j++){
            temp = 0;
            flag = true;
            for(int k = 0; k< 5; k++){
                int nx = i + dx[k];
                int ny = j + dy[k];
                if(visited[nx][ny]){
                    flag = false;
                    break;
                }
                temp+=g[nx][ny];
            }
            if(flag){
                for(int k =0; k< 5; k++){
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    visited[nx][ny] = 1;
                }
                dfs(d+1, cost+temp, visited);
                for(int k =0; k< 5; k++){
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    visited[nx][ny] = 0;
                }
            }
        }
    }
    return;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;

    for(int i = 0; i< n; i++){
        for(int j = 0; j< n; j++){
            cin >> g[i][j];
        }
    }
    int visited[MaxN][MaxN] = {false,};
    dfs(0, 0, visited);
    cout << ans <<endl;
    return 0;
}