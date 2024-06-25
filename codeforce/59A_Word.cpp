#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    string inp;
    cin >> inp;
    int cnt = 0;
    for(int i = 0; i<inp.length(); i++){
        if(inp[i]<95){
            inp[i] = inp[i] + 32;
            cnt++;
        }
    }
    if(cnt>inp.length()-cnt){
        for(int i = 0; i< inp.length(); i++){
            if(inp[i]>=95){
                inp[i] = inp[i] - 32;
            }
        }
    }
    cout << inp;
    return 0;
}