#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int n, m;
string input;
map<string, int> name2idx;
map<int, string> idx2name;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;
    for(int i = 0; i< n; i++){
        cin >> input;
        name2idx[input] = i;
        idx2name[i] = input;
    }
    for(int i = 0; i< m; i++){
        cin >> input;
        if(isdigit(input[0]))
            cout << idx2name[stoi(input)-1] << '\n';
        else
            cout << name2idx[input]+1 << '\n';
    }
    return 0;
}