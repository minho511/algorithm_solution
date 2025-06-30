#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
string s;
string temp;
vector<string> nums;

bool cmp(const string a, const string b){
    if(a.size()!=b.size()) return a.size()<b.size();
    for(int i = 0; i< a.size(); i++){
        if(a[i] == b[i]) continue;
        return a[i] < b[i];
    }
}

void lstripZero(){
    int i;
    for(i = 0; i< temp.size()-1; i++){
        if(temp[i] == '0') continue;
        else break;
    }
    temp.erase(temp.begin(), temp.begin()+i);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    temp = "";
    
    for(int i = 0; i< n; i++){
        cin >> s;
        for(int j = 0; j< s.size(); j++){
            if(s[j]<58){
                temp+=s[j];
                if(j == s.size()-1){
                    if(temp.size()>1)
                        lstripZero();
                    nums.push_back(temp);
                    temp = "";
                }
            }else if(temp.size()>0){
                if(temp.size()>1)
                    lstripZero();
                nums.push_back(temp);
                temp = "";
            }
        }
    }
    sort(nums.begin(), nums.end(), cmp);
    for(auto c : nums) cout << c << '\n';
    return 0;
}
