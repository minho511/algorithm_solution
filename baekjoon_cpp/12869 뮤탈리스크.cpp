#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n;
int ans;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for(int i = 0; i<n; i++)
        cin >> a[i];
    ans = 100001;
    dfs(a, 0);    
    cout << ans;
    return 0;
}