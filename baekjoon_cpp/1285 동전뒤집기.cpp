#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
string s[20];
string s2[20];
int m = 400;
int coin = 0;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;
    int k = 0;
    for(int i =0; i< n; i++){
        cin >> s[i];
        for(int j = 0; j< n; j++){
            if(s[i][j] == 'T') coin|=(1<<k);
            k++;
        }
    }

    for(int i = 0; i < (1<<2*n); i++){
        for(int j = 0; j< n; j++){
            if(i&(1<<j)){ //row
                coin^=(1<<(j*n))
            }    
        }
        for(int k = 0; k< n; k++){
            if(i&(1<<j+n)){ //col

            }
        }
    }

    return 0;
}