#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
    int input;
    for(int i = 0; i<5; i++){
        for(int j = 0; j<5; j++){
            cin >> input;
            if (input == 1){
                cout << abs(i-2)+abs(j-2);
                return 0;
            }
        }
    }
    return 0;
}