class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dist(m, vector<int>(n));
        if(m == 1 || n == 1) return 1;
        for(int i = 1; i<n; i++) dist[0][i] = 1;
        for(int j = 1; j<m; j++) dist[j][0] = 1;
        for(int i = 1; i<m; i++){
            for(int j = 1; j<n; j++){
                dist[i][j] = dist[i][j-1] + dist[i-1][j];
            }
        }
        return dist[m-1][n-1];
    }
};