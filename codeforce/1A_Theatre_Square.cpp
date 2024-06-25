#include<iostream>
#include <algorithm>
using namespace std;

int main(){
    int n, m, a;
    long long t1, t2;
    long long result = 0;
    cin >> n >> m >> a;
    t1 = n/a;
    if(n%a>0) t1++;
    t2 = m/a;
    if(m%a>0) t2++;
    result = t1 * t2;
    
    
    cout << result;
    return 0;
}