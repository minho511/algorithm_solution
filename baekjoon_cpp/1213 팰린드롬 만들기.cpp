#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

string s;
vector<int> cnt(26);
int cntOdd = 0;
string ans = "";
int k = 0;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> s;

    for(auto c : s)
        cnt[c-'A']++;
    
    for(int i = 0; i<26; i++){
        if(cnt[i]%2==1) cntOdd++;
    }
    if(cntOdd>1){
        cout << "I'm Sorry Hansoo\n";
        return 0;
    }
    char keep = -1;
    for(int i = 0; i< 26; i++){
        if(cnt[i]%2==1){
            keep = i+'A';
            cnt[i]--;
        }
        for(int j = 0; j<cnt[i]/2; j++)
            if(cnt[i]>0){
                ans+=(char)(i+'A');
                k++;
        }
    }
    cout << ans;
    if(keep>0) cout << (char)(keep);
    reverse(ans.begin(), ans.end());
    cout << ans;
    return 0;
}