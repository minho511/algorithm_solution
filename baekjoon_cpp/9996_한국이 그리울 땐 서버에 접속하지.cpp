#include <bits/stdc++.h>

using namespace std;

int n;
int i, j, k;
string s, s2;
bool ans;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;
    cin >> s;
    for(int t = 0; t<n; t++){
        cin >> s2;
        ans = true;
        i = 0;
        j = s2.size()-1;
        k = s.size()-1;
        while(s[i] != 42){
            if(s2[i]!=s[i]){
                ans = false;
                break;
            }
            i++;
        }
        if(!ans||s2.size()<s.size()-1) cout << "NE" << '\n';
        else{
            while(s[k] != 42){
                if(s2[j]!=s[k]){
                    ans = false;
                    break;
                }
                k--;
                j--;
            }
            if(!ans) cout << "NE" << '\n';
            else{
                cout << "DA"<<'\n';
            }
        }
    }
    return 0;
}