#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, m, k, j;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;
    cin >> j;
    int front = 1;
    int end = m;
    int result = 0;
    
    for(int i = 0; i< j; i++){
        cin >> k;
        if(k<front){
            k = abs(front-k);
            result+=k;
            front-=k;
            end-=k;
        }
        else if(k > end){
            k = abs(end-k);
            result += k;
            front +=k;
            end +=k;
        }
    }
    cout << result;
    return 0;
}