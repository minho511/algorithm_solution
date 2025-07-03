#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n;
string s;
int g[20] = {0,};
vector<pair<int, int>> pairs;
vector<pair<int, int>> pairs2;

int ans = -pow(2, 31);
int l, r, jj;

void combi(int start, vector<int> &b, int k){
    
    if(b.size() == k){
        vector<int> idx;
        vector<bool> visited(n/2, false);
        vector<bool> check(n/2, false);
        
        for(int i = 0; i< b.size(); i++){
            if(k>1&&i<b.size()-1){
                if(abs(b[i]-b[i+1])==1){
                    return;
                }
            }
            idx.push_back(b[i]);
            check[b[i]] = true;
        }
        for(int i = 0; i< n/2; i++){
            if(check[i]) continue;
            else idx.push_back(i);
        }        
        copy(pairs.begin(), pairs.end(), pairs2.begin());
    
        for(int i = 0; i< idx.size(); i++){
            int j = idx[i];
            visited[j] = true;
            tie(l, r) = pairs2[j];
            if(g[j] == '+') {l = l+r;}
            else if(g[j] == '-') {l = l-r;}
            else if(g[j] == '*') {l = l*r;}
            pairs2[j].first = l;
            pairs2[j].second = l;
            jj = j-1;
            while(jj>0 && visited[jj]){
                pairs2[jj].first = l;
                pairs2[jj].second = l;
                pairs2[jj-1].second = l;
                jj-=1;
            }
            jj = j+1;
            while(jj<idx.size() && visited[jj]){
                pairs2[jj].first = l;
                pairs2[jj].second = l;
                pairs2[jj+1].first = l;
                jj+=1;
            }
            if(j<idx.size()-1) pairs2[j+1].first = l;
            if(j>0) pairs2[j-1].second = l;
        }
        ans = max(ans, l);
        return;
    }
    for(int i = start + 1; i <n/2; i++){
        b.push_back(i);
        combi(i, b, k);
        b.pop_back();
    }
    return;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    cin >> s;
    if(n == 1) {cout << s; return 0;}
    int k = 0;
    for(int i = 1; i< n-1; i+=2){
        g[k] = s[i];
        pairs.push_back({s[i-1]-'0', s[i+1]-'0'});
        pairs2.push_back({s[i-1]-'0', s[i+1]-'0'});
        k++;
    }    
    for(int i = 0; i<n/2; i++){
        vector<int>b;
        combi(-1, b, i);
    }
    cout << ans;
    
    return 0;
}