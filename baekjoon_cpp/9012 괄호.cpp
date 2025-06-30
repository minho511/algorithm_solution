#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n;
string s;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    while(n--){
        bool VPS = true;
        cin >> s;
        vector<char> vec;
        for(auto c : s){
            if(c == '(') vec.push_back(c);
            else if(vec.size() == 0 && c == ')'){
                    VPS = false;
                    break;
            }else if(c == ')'){ 
                if(vec.size() == 0){
                    VPS = false;
                    break;
                }else{
                    vec.pop_back();
                }
            }
        }
        if(vec.size()) VPS = false;

        if(VPS) cout << "YES\n";
        else cout << "NO\n";
    }

    return 0;
}