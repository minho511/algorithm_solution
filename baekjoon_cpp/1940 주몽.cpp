#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n, m;
int i, j;
int ans = 0;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    cin >> m;
    vector<int> vec(n);
    for(auto &e: vec) cin >> e;
    sort(vec.begin(), vec.end());
    i = 0;
    j = n-1;
    while(i<j){
        if(vec[i]+vec[j] == m){
            i++;
            j--;
            ans++;
        }else if(vec[i]+vec[j] > m){
            j--;
        }else if(vec[i]+vec[j] < m){
            i++;
        }
    }
    cout << ans;
    
    return 0;
}