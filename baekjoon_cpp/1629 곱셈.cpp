#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll a, b, c;

ll mysol(ll a, ll b){
    if(b == 1) return a%c;
    ll ans = mysol(a, b/2);
    ans = (ans*ans)%c;
    if(b%2) ans = (ans*a)%c;
    return ans;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> a >> b >> c;
    cout << mysol(a, b);
    return 0;
}