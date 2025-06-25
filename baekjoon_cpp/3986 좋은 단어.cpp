#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n;
string s;
int ans = 0;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    for(int i = 0; i<n; i++){
        cin >> s;
        vector<char> stack;
        for(auto c : s){
            if (stack.size()==0)
                stack.push_back(c);
            else{
                if(stack.back() != c){
                    stack.push_back(c);
                }else
                    stack.pop_back();
            }
        }
        if(stack.size()==0) ans++;
    }    
    cout << ans;
    return 0;
}