#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main(){
    int c = 0;
    string a, b;
    int aa, bb;
    string ans = "";
    cin >> a >> b;
    if(a.size()<b.size()) swap(a, b);
    while(a.size()>b.size()) b = '0'+b;
    for(int i = a.size()-1; i>=0; i--){
        aa = a[i]-'0';
        bb = b[i]-'0';
        ans = char(((aa+bb+c)%10)+'0') + ans;
        c = (aa+bb+c)/10;
    }
    if(c) ans = '1'+ans;
    cout << ans;
    return 0;
}