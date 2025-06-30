#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

string s;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    while(true){
        getline(cin, s);
        if(s == ".") break;
        bool balanced = true;
        stack<char> stk;
        for(auto c : s){
            if(c == '(' || c == '[') stk.push(c);
            else if(c == ')'){
                if(stk.empty()){
                    balanced = false;
                    break;
                }else{
                    auto temp = stk.top();stk.pop();
                    if(temp == '['){
                        balanced = false;
                        break;
                    }
                }
            }else if(c == ']'){
                if(stk.empty()){
                    balanced = false;
                    break;
                }else{
                    auto temp = stk.top();stk.pop();
                    if(temp == '('){
                        balanced = false;
                        break;
                    }
                }
            }
        }
        if(!stk.empty()) balanced = false;
        
        if(balanced) cout << "yes\n";
        else cout << "no\n";
    }
    
    return 0;
}