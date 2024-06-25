#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int n;
    int cnt = 0;
    string inp;

    cin >> n;
    cin >> inp;
    
    for(int i = 1; i< n; i++){
        if(inp[i] == inp[i-1]){
            cnt++;
        }
    }
    cout << cnt;
    return 0;
}