class Solution {
public:

    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {

        int N = maze.size();
        int M = maze[0].size();
        vector<vector<int>> dist(N, vector<int> (M));
        dist[entrance[0]][entrance[1]]++;
        vector<int> dx = {-1, 1, 0, 0};
        vector<int> dy = {0, 0, 1, -1};
        int cx,cy, nx, ny;
        vector<int> c ;
        deque<vector<int>> queue;
        queue.push_back(entrance);
        while(queue.size()>0){
            c = queue[0];
            queue.pop_front();
            cx = c[0];
            cy = c[1];
            for(int i = 0; i< 4; i++){
                nx = cx+dx[i];
                ny = cy+dy[i];
                if((nx<0||ny<0)||(nx>=N||ny>=M)) continue;
                if(maze[nx][ny] == '+') continue;
                if(dist[nx][ny] > 0) continue;
                queue.push_back({nx, ny});
                dist[nx][ny] = dist[cx][cy]+1;
                if((nx==0||ny==0)||(nx==N-1||ny==M-1)) return dist[nx][ny]-1;
            }
        }
        return -1;
    }
};