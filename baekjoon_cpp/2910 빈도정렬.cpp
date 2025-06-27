#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, c, k;
map<int, int> cntMap;
map<int, int> orderMap;

bool cmp(const pair<int, int>& a, const pair<int, int>& b){
    if(a.second == b.second) return orderMap[a.first] < orderMap[b.first];
    return a.second > b.second;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> c; 
    for(int i = 0; i< n; i++){
        cin >> k;
        if(cntMap.find(k) == cntMap.end()){
            cntMap.insert({k, 1});
            orderMap.insert({k, i});
        }
        else{
            cntMap[k]++;
        }
    }
    vector<pair<int, int>> cntVec(cntMap.begin(), cntMap.end());
    sort(cntVec.begin(), cntVec.end(), cmp);
    int a, b;
    for(auto c : cntVec){
        tie(a, b) = c;
        for(int i = 0; i< b; i++){
            cout << a << ' ';
        }
    }
    return 0;
}