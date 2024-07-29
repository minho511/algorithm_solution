class Solution {
public:
    void dfs(vector<bool>& visited, vector<vector<int>>& rooms, int curRoom){
        visited[curRoom] = 1;
        for(auto k : rooms[curRoom]){
            if(!visited[k]){
                dfs(visited, rooms, k);
            }
        }
    }

    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<bool> visited(n);
        bool answer = 0;
        
        dfs(visited, rooms, 0);
        if(accumulate(visited.begin(), visited.end(), 0) == n) answer = 1;    
        return answer;
    }
};