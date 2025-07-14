#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MaxN = 987654321;
int n, a, b;
vector<int> g[11];
int popl[11] = {0, };
bool visited[11] = {false,};
int ans = MaxN;

bool region[11] = {0, };

pair<int, int> dfs(int x, int r){
    visited[x] = true;
    pair<int, int> res = {1, popl[x]};
    for(auto c: g[x]){
        if(region[c] != r) continue;
        if(visited[c]) continue;
        pair<int, int> _temp = dfs(c, r);
        res.first += _temp.first;
        res.second += _temp.second;
    }
    return res;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    for(int i = 1; i<= n; i++) cin >> popl[i];
    for(int i = 1; i<= n; i++){
        cin >> a;
        for(int j = 0; j < a; j++){
            cin >> b;
            g[i].push_back(b);
        }
    }
    for(int i = 1; i < (1<<n)-1; i++){
        memset(visited, 0, sizeof(visited));
        memset(region, 0, sizeof(region));
        a = -1;
        b = -1;
        for(int j = 0; j < n; j++){
            if(i&(1<<j)){region[j+1] = 1; a = j+1;}
            else {b = j+1;}
        }
        pair<int, int> p1 = dfs(a, 1);
        pair<int, int> p2 = dfs(b, 0);
        if(p1.first+p2.first == n) ans = min(ans, abs(p1.second-p2.second));
    }
    if(ans<MaxN) cout << ans;
    else cout << -1;
    return 0;
}