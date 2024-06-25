#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int a, b;
    cin >> a >> b;
    int result = 0;
    while(a<=b){
        a = a*3;
        b = b*2;
        result++;
    }
    cout <<result;
    return 0;
}