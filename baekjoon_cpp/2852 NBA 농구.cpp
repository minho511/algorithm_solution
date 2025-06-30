#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n;
string s;

int h2m(string s){
    int h = stoi(s.substr(0, 2));
    int m = stoi(s.substr(3, 5));
    return h*60+m;
}
string m2h(int m){
    string temp = "";
    int h = m/60;
    m = m%60;
    if(h/10<1) temp+="0";
    temp+=to_string(h);
    temp+=":";
    if(m/10<1) temp+="0";
    temp+=to_string(m);
    return temp;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    int pointB = 0;
    int pointA = 0;
    int timeA = 0;
    int timeB = 0;
    int timeD = 0;
    int sA = 0;
    int sB = 0;
    int win = -1;
    int team;
    while(n--){
        cin >> team >> s;

        if(team == 1) pointA++;
        else pointB++;

        if(pointA > pointB && win != 1){
            sA = h2m(s);
            win = 1;
        }else if(pointB > pointA && win != 2){
            sB = h2m(s);
            win = 2;
        }else if(pointA == pointB){ // point A == point B
            timeD = h2m(s);
            if(win == 1) timeA += timeD-sA;
            if(win == 2) timeB += timeD-sB;
            sA = 0;
            sB = 0;
            win = -1;
        }
    }
    if(pointA>pointB) timeA += 48*60-sA;
    if(pointB>pointA) timeB += 48*60-sB;
    cout << m2h(timeA) << '\n';
    cout << m2h(timeB) << '\n';
    return 0;
}