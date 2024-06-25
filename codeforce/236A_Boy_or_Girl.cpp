#include<algorithm>
#include<iostream>


using namespace std;

int main(){
    string input;
    string answer1 = "CHAT WITH HER!";
    string answer2 = "IGNORE HIM!";
 
    cin >> input;
    sort(input.begin(), input.end());
    input.erase(unique(input.begin(), input.end()), input.end());
    if (input.length()%2==1) cout << answer2;
    else cout << answer1;

    return 0;
}