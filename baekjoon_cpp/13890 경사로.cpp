#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n, l, a;
int g1[101][101];
int g2[101][101];
int cnt;
int tot = 0;
void cross(int road[][101]){
    for(int i = 0; i < n; i++){
        cnt = 1;
        int j;
        for(j = 0; j< n-1; j++){
            if(road[i][j] == road[i][j+1]) cnt++;
            else if(road[i][j+1]-road[i][j]==1 && cnt>=l) cnt = 1;
            else if(road[i][j+1]-road[i][j]==-1 && cnt>=0) cnt = -l+1;
            else break;
        }
        if(j == n-1 && cnt >= 0) tot++;
    }
    return;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> l;
    for(int i = 0; i< n; i++){
        for(int j =0; j< n; j++){
            cin >> g1[i][j];
            g2[j][i] = g1[i][j];
        }
    }
    cross(g1);
    cross(g2);
    cout << tot;
    return 0;
}