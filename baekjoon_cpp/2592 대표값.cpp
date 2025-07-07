#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int k;
int bin[100];
int accm = 0;
int maxIdx = -1;
int maxBin = -1;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    for(int i = 0; i< 10; i++){
        cin >> k;
        accm += k;
        bin[k/10]++;
        if(maxBin < bin[k/10]){
            maxBin = bin[k/10];
            maxIdx = k;
        }
    }
    cout << accm/10 << '\n';
    cout << maxIdx << '\n';
    return 0;
}