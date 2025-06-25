#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n;
ll i, cnt;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    while(cin >> n){
        i = 1;
        cnt = 1;
        while(i%n != 0){
            i = ((i*10)+1)%n;
            cnt++;
        }
        cout << cnt<< '\n';
    }

    return 0;
}