#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    int n;
    cin >> n;
    int result = 0;
    for(int i = 5; i>1; i--){
        result = result + n/i;
        n = n%i;
    }
    cout << n+result;
    return 0;
}