class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        int c;
        vector<int> r;
        int p;
        bool remain = 0;
        r.push_back(asteroids.back());
        asteroids.pop_back();
        while(asteroids.size() > 0){
            c = asteroids.back();
            asteroids.pop_back();
            if(r.size()==0){
                r.push_back(c);
                continue;
            }
            p = r.back();
            r.pop_back();
            if(c*p>0){
                r.push_back(p);
                r.push_back(c);
            }else if(c<0 && p>0){
                r.push_back(p);
                r.push_back(c);
            }else if(c>0 && p<0){
                if(-p<c){
                    asteroids.push_back(c);
                }else if(-p==c){
                    continue;
                }else if(-p>c){
                    r.push_back(p);
                }
            }
        }
        reverse(r.begin(), r.end());
        return r;
    }
};