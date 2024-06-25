#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    string inp;
    char check;
    cin >> inp;
    

    for(int i = 0; i<inp.length(); i++){
        
        if(inp[i]<95) inp[i] = inp[i]+32;
        check = inp[i];
        if((check=='a')||(check=='o')||(check=='y')||(check=='e')||(check=='u')||(check=='i')){
            continue;
        }else{
            cout << '.';
            cout << check;
        }
    }
    return 0;
}