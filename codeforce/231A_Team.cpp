#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int t;
    int result = 0;
    int a, b, c;

    cin >> t;
    for(int i = 0; i<t; i++){
        cin >> a >> b >> c;
        if (a+b+c>=2) result++;
    }
    cout << result;
    
    return 0;
}