class Solution {
public:
    void checkConnect(int now, int nSize, vector<vector<int>>& isConnected, vector<int>& g, int numConnection){
        for(int i = 0; i<nSize; i++){
            if(i!=now && isConnected[now][i] == 1){
                if(g[i]!=0) continue;
                g[i] = numConnection;
                checkConnect(i, nSize, isConnected, g, numConnection);
            }
        }
    }
    int findCircleNum(vector<vector<int>>& isConnected) {
        int nSize = isConnected.size();
        vector<int> g(nSize);
        int numConnection = 1;
        for(int i = 0; i<nSize; i++){
            if(g[i] == 0){
                g[i] = numConnection;
                checkConnect(i, nSize, isConnected, g, numConnection);
                numConnection++;
            }
        }    
        return numConnection-1; 
    }
};