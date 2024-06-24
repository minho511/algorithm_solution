#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    long long t, n, a, b, k, m;
    long long res;
    cin >> t;
    
    for(int i = 0; i< t; i++){
        cin >> n >> a >> b;
        m = n;
        if(b<n) m = b;
        res = 0;
        k = (1-2*a+2*b)/2;
        if(k > m) k = m;
        if(k <= 0) k = 0;
        
        res = b*k-k*(k-1)/2 + (n-k)*a;
        
        cout << res <<'\n';
    }

    return 0;
}