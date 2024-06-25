#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    string input;
    int t;
    int x = 0;
    string add1 = "X++";
    string add2 = "++X";
    
    cin >> t;
    for(int i = 0; i< t; i++){
        cin >> input;
       if(!(input.compare(add1)*input.compare(add2))) x++;
        else x--;
    }
    cout << x;
    return 0;
}