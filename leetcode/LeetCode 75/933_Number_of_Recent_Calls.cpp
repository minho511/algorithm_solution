class RecentCounter {
public:
    deque<int> que;

    int ping(int t) {
        int t_lim = t-3000;
        que.push_back(t);
        for(auto x: que){
            if(x<t_lim ){
                que.pop_front();
            }else{
                break;
            }
        }
        return que.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */