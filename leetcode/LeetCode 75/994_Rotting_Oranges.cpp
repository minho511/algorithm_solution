class Solution {
public:
    void bfs(vector<vector<int>>& grid, int i, int j, int n, int m, deque<pair<int, int>>& dq, vector<vector<int>>& countMap){
            // bfs
            if(i-1>=0){//u
                if(grid[i-1][j] == 1){
                    grid[i-1][j] = 2;
                    countMap[i-1][j] = countMap[i][j]+1;
                    dq.push_back(make_pair(i-1, j));
                }
            }
            if(i+1<n){//d
                if(grid[i+1][j] == 1){
                    grid[i+1][j] = 2;
                    countMap[i+1][j] = countMap[i][j]+1;
                    dq.push_back(make_pair(i+1, j));
                }
            }
            if(j+1<m){//r
                if(grid[i][j+1] == 1){
                    grid[i][j+1] = 2;
                    countMap[i][j+1] = countMap[i][j]+1;
                    dq.push_back(make_pair(i, j+1));
                }
            }
            if(j-1>=0){//l
                if(grid[i][j-1] == 1){
                    grid[i][j-1] = 2;
                    countMap[i][j-1] = countMap[i][j]+1;
                    dq.push_back(make_pair(i, j-1));
                }
            }
    }
    
    int orangesRotting(vector<vector<int>>& grid) {
        
        int n = grid.size();
        int m = grid[0].size();
        int ans = 0;
        deque<pair<int, int>> dq;
        vector<vector<int>> countMap(n, vector<int>(m));
        for(int i = 0; i< n; i++){
            for(int j = 0; j<m; j++){
                if(grid[i][j] == 2)
                    dq.push_back(make_pair(i, j));
            }
        }
        while(!dq.empty()){
            auto p = dq[0];
            dq.pop_front();
            bfs(grid, p.first, p.second, n, m, dq, countMap);
        }

        for(int i = 0; i< n; i++){
            for(int j = 0; j<m; j++){
                if(grid[i][j] == 1)
                    return -1;
                ans = max(countMap[i][j], ans);
            }
        }
        return ans;
    }  
    
};