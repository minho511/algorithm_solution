#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

string ans = "";
const int MaxN = 64;
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};
string g[MaxN];
bool visited[MaxN][MaxN] = {false,};

int n, x, y, k, t;

void dfs(int x, int y, int n){
    bool all0 = true;
    bool all1 = true;
    for(int i = x; i < x+n; i++){
        for(int j = y; j < y+n; j++){
            if(g[i][j] != '0') all0 = false;
            if(g[i][j] != '1') all1 = false;
        }
    }
    if(all0) ans+='0';
    if(all1) ans+='1';
    if(!all0 && !all1){
        ans+='(';
        dfs(x, y, n/2);
        dfs(x, y+n/2, n/2);
        dfs(x+n/2, y, n/2);
        dfs(x+n/2, y+n/2, n/2);
        ans+=')';
    }
    return;
}

void sol(){
    
    cin >> n;
    for(int i = 0; i< n; i++){
        cin >> g[i];
    }
    dfs(0, 0, n);

    cout << ans;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    sol();
    return 0;
}