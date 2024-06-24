#include<iostream>
#include<algorithm>

using namespace std;

void solve(){
    int t;
    int x, y, z;
    int xs=0, ys=0, zs = 0;
    cin >> t;
    for(int i = 0; i<t; i++){
        cin >> x >> y >> z;
        xs += x;
        ys += y;
        zs += z;
    }
    if(xs==0 && ys==0 && zs==0) cout << "YES";
    else cout << "NO";
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}