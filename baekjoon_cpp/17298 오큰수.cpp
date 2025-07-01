#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, k;
vector<int> nums;
vector<int> vec = {0};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    vector<int> results(n, -1);
    for(int i = 0; i < n; i++){
        cin >> k;
        nums.push_back(k);
    }
    int i = 1;
    while(vec.size() && i < n){
        while(vec.size() && nums[vec.back()] < nums[i]){
            results[vec.back()] = nums[i];
            vec.pop_back();
        }
        vec.push_back(i++);
    }
    for(auto c: results) cout << c << ' ';
    return 0;
}