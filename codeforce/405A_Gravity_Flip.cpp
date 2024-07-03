#include <bits/stdc++.h>
#define ll long long

using namespace std;

int n, a;
vector<int> v;

bool compare(const int a, const int b){
    return a<b;
}

void solve(){
    cin >> n;
    for(int i = 0; i<n; i++){
        cin >> a;
        v.push_back(a);
    }
    sort(v.begin(), v.end(), compare);
    for(int i = 0; i<n; i++){
        cout << v[i] << " ";
    }

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    solve();
    return 0;
}