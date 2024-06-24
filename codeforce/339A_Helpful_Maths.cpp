
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main(){
    string input;
    string a;
    vector<int> vec;
    int temp;
    cin >> input;
    for (int i = 0; i< input.length(); i = i+2){
        a = input[i];
        temp = stoi(a);
        vec.push_back(temp);
    }
    sort(vec.begin(), vec.end());
    for(int i = 0; i<vec.size(); i++){
        if(i == 0) cout << vec[i];
        else cout << "+" << vec[i];
    }
    return 0;
}