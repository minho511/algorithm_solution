#include <bits/stdc++.h>
using namespace std;

int n, k, input;
int s = 0;
int ans = -10000000;
int t;

int main(){
    ios_base::sync_with_stdio(false);
    
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> k;
    vector<int> vec(n+1);

    for (int i = 1; i < n+1; i++){
        cin >> input;
        s+=input;
        vec[i] = s;
        if(i>=k){
            t  = vec[i]-vec[i-k];
            if(t>ans)
                ans = t;
        }
    }
    cout << ans;
    return 0;
}