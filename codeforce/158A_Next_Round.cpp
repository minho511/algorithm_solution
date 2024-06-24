#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

bool cmp(int a, int b){return a>b;}

int main(){
    int n, k;
    cin >> n >> k;
    int inp;
    int t;
    vector<int> arr = {};
    int result = 0;
    for (int i = 0; i< n; i++){
        cin >> inp;
        arr.push_back(inp);
    }

    t = arr[k-1];

    for(int i = 0; i<n; i++){
        if((arr[i] >= t)&&(arr[i]>0)) result++;
    }

    cout << result ;
    
    return 0;
}