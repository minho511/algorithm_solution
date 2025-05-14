#include <algorithm>
#include <iostream>
using namespace std;

int main(){
    string input1;
    string input2;
    int c1 = 0;
    int c2 = 0;

    cin >> input1;
    cin >> input2;
    
    for(int i = 0; i<input2.length(); i++){
        c1 = input1[i];
        c2 = input2[i];
        if(c1<97) c1 = c1+32;
        if(c2<97) c2 = c2+32;
        if(c1<c2){
            cout << -1;
            return 0;
        }else if(c1>c2){
            cout << 1;
            return 0;
        }
    }
    cout << 0;
    return 0;
}