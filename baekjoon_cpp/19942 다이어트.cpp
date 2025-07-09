#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
int mp, mf, ms, mv;
int p, f, s, v, c;
int g[15][5];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    cin >> mp >> mf >> ms >> mv;
    bool check = false;
    int minCost = 8000;
    vector<vector<int>> res;
    for(int i = 0; i< n ; i++){
        for(int j = 0; j < 5; j++) cin >> g[i][j];
    }
    for(int i = 0 ; i < (1<<n); i++){
        p = 0; f = 0; s = 0; v = 0; c = 0;
        vector<int> t;
        for(int j = 0; j < n; j++){
            if(i & (1<<j)){
                p += g[j][0]; f += g[j][1]; s += g[j][2]; v += g[j][3]; c += g[j][4];
                t.push_back(j+1);
            }
        }
        if(p>=mp && f>=mf && s >=ms && v>=mv && minCost >= c){
            check = true;
            if(minCost>c){
                res.clear();
                minCost = c;
                res.push_back(t);
            }else res.push_back(t);
            
        }
    }
    if(check){
        sort(res.begin(), res.end());
        cout << minCost << '\n';
        for(int i = 0; i< res[0].size(); i++) cout << res[0][i] << ' ';
    }else{
        cout << -1;
    }
    
    return 0;
}