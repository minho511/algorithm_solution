#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int a[3] = {1,2,3};
int n = 3, r = 3;
void print(){
    for(int i = 0; i< r; i++)
        cout << a[i] << ' ';
    cout << '\n';
}

void makePermutation(int n, int r, int depth){
    if(r==depth){
        print();
        return;
    }
    for(int i = depth; i < n; i++){
        swap(a[i], a[depth]);
        makePermutation(n, r, depth + 1);
        swap(a[i], a[depth]);
    }
    return;
}

int main(){
    makePermutation(n, r, 0);
    return 0;
}

// void printV(vector<int> &v){
//     for(int i = 0; i < v.size(); i++)
//         cout << v[i] << ' ';
//     cout << '\n';
// }

// int main(){
//     ios_base::sync_with_stdio(false);
//     cin.tie(NULL);
//     cout.tie(NULL);
    
//     int a[3] = {1,2,3};
//     vector<int> v;
//     for(int i = 0; i < 3; i++) v.push_back(a[i]);
//     do{
//         printV(v);
//     }while(next_permutation(v.begin(), v.end()));

//     return 0;
// }