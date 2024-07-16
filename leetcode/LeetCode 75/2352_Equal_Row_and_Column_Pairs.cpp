class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>> mr;
        vector<vector<int>> mc;
        vector<int> r(n);
        vector<int> c(n);
        for(int i = 0; i< n; i++){
            
            for(int j = 0; j<n; j++){
                r[j] = grid[i][j];
                c[j] = grid[j][i];
            }
            mr.push_back(r);
            mc.push_back(c);
        }
        int cnt = 0;
        for(int i = 0; i<n; i++){
            for(int j = 0; j<n; j++){
                if(mr[i]==mc[j]){
                    cnt++;
                }
            }
        }
        return cnt;
    }
};