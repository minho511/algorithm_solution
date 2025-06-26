#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n,x;
int cnt = 0;
int i = 0;
int j;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    j = n-1;
    vector<int> vec(n);
    for(auto &c : vec) cin >> c;
    sort(vec.begin(), vec.end());
    cin >> x;
    while(i<j){
        if(vec[i]+vec[j]){

        }
        int k = vec[i]+vec[j];
        if(k == x){
            cnt++;
            i++;
            j--;
        }else if(k < x){
            i++;
        }else if(k > x){
            j--;
        }
    }
    cout << cnt;
    return 0;
}