#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n, k, r, root;
vector<int> tree[50];
int cnt = 0;

void postOrder(int here){
    if(here == r) return;
    if(tree[here].size() == 0){
        cnt++;
        return;
    }
    for(int node : tree[here]){
        if(node == r){
            if(tree[here].size() == 1){
                cnt++;
                return;
            }
            else continue;
        }
            
        postOrder(node);
    }
    return;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    for(int i = 0; i< n; i++){
        cin >> k;
        if(k == -1) root = i;
        else tree[k].push_back(i);
    }
    cin >> r;
    postOrder(root);
    cout << cnt;
    return 0;
}