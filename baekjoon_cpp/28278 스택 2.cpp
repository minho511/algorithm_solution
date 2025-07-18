#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<int> st;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n, a, x;
    cin >> n;
    while(n--){
        cin >> a;
        if(a == 1){
            cin >> x;
            st.push_back(x);
        }else if(a == 2){
            if(st.size()>0){
                cout << st.back()<<'\n'; st.pop_back();
            }else cout << -1<<'\n';
        }else if(a == 3){
            cout << st.size()<<'\n';
        }else if(a == 4){
            cout << (st.size()? 0:1)<<'\n';
        }else if(a == 5){
            if(st.size()>0) cout << st.back()<<'\n';
            else cout << -1<<'\n';
        }
    }

    

    return 0;
}