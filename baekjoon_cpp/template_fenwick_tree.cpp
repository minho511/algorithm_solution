#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
vector<int> tree;

void update(int index, int value){
    while(index < tree.size()){
        tree[index] += value;
        index += index & -index;
    }
}

int sum(int index){
    int ret = 0;
    while(index > 0){
        ret += tree[index];
        index -= index & -index;
    }
    return ret;
}

int rangeQuery(int left, int right){
    return sum(right) - sum(left-1);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    vector<int> data = {3, 4, 10, 11};
    n = data.size();
    tree.resize(n+1, 0);

    for(int i = 0; i< n; i++){
        update(i+1, data[i]);
    }
    

    return 0;
}