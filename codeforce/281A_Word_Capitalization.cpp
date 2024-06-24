#include <algorithm>
#include <iostream>
using namespace std;


int main(){
    string input;
    cin >> input;
    if(input[0]>=97) cout << (char)(input[0]-32) << input.substr(1, input.length());
    else cout << input;
    
    return 0;
}