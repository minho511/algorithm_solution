#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n, m, a, b;
const int MaxN = 10001;
vector<int> g[MaxN];
bool visited[MaxN] = {false,};
int cnt;

void hacking(int here){
    cnt++;
    visited[here] = 1;
    for(int c : g[here]){
        if(visited[c]) continue;
        hacking(c);
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int ans = 0;
    vector<pair<int,int>> results;
    cin >> n >> m;

    for(int i = 0; i< m; i++){
        cin >> a >> b;
        g[b].push_back(a);
    }

    for(int i = 1; i< n+1; i++){
        //hack i
        cnt = 0;
        memset(visited, false, sizeof(visited));
        hacking(i);
        ans = max(ans, cnt);
        results.push_back({i, cnt});
    }
    for(auto c : results){
        if(c.second == ans) cout <<  c.first << ' ';
    }
    return 0;
}