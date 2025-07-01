#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MaxN = 51;
int visited[MaxN][MaxN] = {0,};
int g[MaxN][MaxN] = {0, };
int n, m, x, y, cx, cy, dist, ans;
vector<pair<int, int>> chicken;
vector<pair<int, int>> home;

void combi(int start, vector<int> &b){
    if(b.size() == m){
        dist = 0;
        for(auto c : home){
            tie(x, y) = c;
            int mini = n*2+1;
            for(int i = 0; i< m; i++){
                tie(cx, cy) = chicken[b[i]];
                mini = min(mini, abs(x-cx)+abs(y-cy));
            }
            dist+=mini;
        }
        ans = min(ans, dist);
        return;
    }
    for(int i = start + 1;  i < chicken.size(); i++){
        b.push_back(i);
        combi(i, b);
        b.pop_back();
    }
    return;
}

void sol(){
    ans = 1000001;
    cin >> n >> m;
    for(int i = 0; i< n; i++){
        for(int j = 0; j<n; j++){
            cin >> g[i][j];
            if(g[i][j] == 2)
                chicken.push_back({i, j});
            else if(g[i][j] == 1)
                home.push_back({i, j});
        }
    }
    vector<int> b; 
    combi(-1, b);
    cout << ans;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    sol();
    return 0;
}