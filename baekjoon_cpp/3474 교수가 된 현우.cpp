#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int t, n;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> t;
    while(t--){
        int ans = 0;
        cin >> n;
        for(int i = 5; i <= n; i*=5){
            ans+= n/i;
        }
        cout << ans << '\n';
    }    
    return 0;
}