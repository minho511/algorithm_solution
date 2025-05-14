#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    int m, n, t;
    cin >> m >> n;
    if((m/2)<(n/2)){t = m;m = n;n = t;}
    cout << (m/2)*n + (m%2)*(n/2);
    return 0;
}