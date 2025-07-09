#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
int ans = 100;
int attack[6][3] = {{9, 3, 1}, {9, 1, 3}, {1, 9, 3}, {1, 3, 9}, {3, 1, 9}, {3, 9, 1}};
int visited[60][60][60] = {0,};
int a[3] = {0,};
queue<vector<int>> q;

int bfs(int h1, int h2, int h3){
    q.push({h1, h2, h3});
    visited[h1][h2][h3] = 1;
    while(q.size()){
        auto v = q.front(); q.pop();
        h1 = v[0]; h2 = v[1]; h3 = v[2];
        if(h1 <= 0 && h2 <= 0 && h3 <= 0){
            return visited[h1][h2][h3]-1;
        }
        for(int i = 0; i< 6; i++){
            int nh1 = h1-attack[i][0];
            int nh2 = h2-attack[i][1];
            int nh3 = h3-attack[i][2];
            nh1 = max(0, nh1); nh2 = max(0, nh2); nh3 = max(0, nh3);
            if(visited[nh1][nh2][nh3]) continue;
            visited[nh1][nh2][nh3] = visited[h1][h2][h3]+1;
            q.push({nh1, nh2, nh3});
        }    
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int h1(0), h2(0), h3(0);
    cin >> n;
    if(n == 3) cin >> h1 >> h2 >> h3;
    else if(n == 2) cin >> h1 >> h2;
    else if(n == 1) cin >> h1;
    cout << bfs(h1, h2, h3); 
    return 0;
}