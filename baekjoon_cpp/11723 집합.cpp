#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int S = 0;
string input;
int m, x; 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> m;
    while(m--){
        cin >> input;
        if(input != "all" && input != "empty") cin >> x;
        if(input[0] == 'a'&&input[1] == 'd') S |= (1<<x);
        else if(input[0] == 'r') S &= ~(1<<x);
        else if(input[0] == 'c') if(S&(1<<x)){ cout << 1 << '\n';}else{cout << 0 << '\n';}
        else if(input[0] == 't') S ^= (1<<x);
        else if(input[0] == 'a' && input[1] == 'l') S = (1<<21)-1;
        // else if(input[0] == 'e') S &= ~((1<<21)-1);
        else S = 0;
    }

    return 0;
}