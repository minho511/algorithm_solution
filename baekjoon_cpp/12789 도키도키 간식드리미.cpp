#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
int n, k;
vector<int> v;
int temp;
int main(){
    temp = 1;
    cin >> n;
    for(int i = 0; i< n; i++){
        cin >> k;
        if(k==temp) temp++;
        else v.push_back(k);
        while(v.size()>0 && v.back() == temp){
            temp++;
            v.pop_back();
        }
    }
    cout << (!v.size() ? "Nice" : "Sad");
    return 0;
}