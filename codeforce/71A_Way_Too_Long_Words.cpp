#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    string a;
    string result;
    int l;
    int t;
    cin >>t;
    for(int i = 0; i< t; i++){
        cin >> a;
        l = a.length();
        if(l > 10) cout << a[0] << l-2 <<a[l-1]<<'\n';
        else cout << a <<'\n';
    }
    return 0;
}