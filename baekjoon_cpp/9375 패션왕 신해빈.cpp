#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int t, n;
string s1, s2;
int ans;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> t;
    for(int i = 0; i<t; i++){
        map<string, int> m;
        ans = 1;
        cin >> n;
        for(int j = 0; j< n; j++){
            cin >> s1 >> s2;
            if(m.find(s2) == m.end()) m[s2]=1;
            else m[s2]++;
        }
        for(auto iter = m.begin(); iter!=m.end(); iter++){
            ans = (iter->second+1) * ans;
        }
        cout << ans-1 << '\n';
    }           
    return 0;
}