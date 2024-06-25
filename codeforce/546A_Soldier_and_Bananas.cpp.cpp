#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    int k, n, w;
    int result;
    cin >> k >> n>> w;
    result = k*(w)*(w+1)/2-n;
    if(result>=0) cout << result;
    else cout << 0;
    return 0;
}