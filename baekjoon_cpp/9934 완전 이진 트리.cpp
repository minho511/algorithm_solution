#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, t;

vector<int> adj[1025];
int visited[1025];
vector<int> inputs;
vector<int> elevel[1025];
map<int, int> m;
int p = 0;

void inOrder(int here, int depth){
    if(visited[here]) return;
    if(adj[here].size() == 2){
        inOrder(adj[here][0], depth+1);
        elevel[depth].push_back(here);
        visited[here] = 1;
        m[here] = inputs[p]; p++;
        inOrder(adj[here][1], depth+1);
    }else{
        visited[here] = 1;
        m[here] = inputs[p]; p++;
        elevel[depth].push_back(here);
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int root = 1;
    int k = 0;
    cin >> n;
    for(int i = 1; i<pow(2, n-1); i++){
        adj[i].push_back(2*i);
        adj[i].push_back(2*i+1);
    }

    for(int i = 0; i< pow(2, n)-1; i++){
        cin >> k;
        inputs.push_back(k);
    }
    inOrder(root, 0);
    
    for(int i = 0; i<n; i++){
        for(auto c : elevel[i]){
            cout << m[c] << ' ';
        }
        cout << endl;
    }
    return 0;
}