// 내풀이
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        set<int> arrset(arr.begin(), arr.end());
        int n = arr.size();
        set<int> occur;
        vector<int> occurv;
        for(auto x : arrset){
            auto c = count(arr.begin(), arr.end(), x);
            occur.insert(c);
            occurv.push_back(c);
        }

        return occur.size() == occurv.size();

    }
};

// 참고할만한 코드 : unordered_map 을 사용

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        std::unordered_map<int, int> O;
        for (auto e : arr)
        {
            if (O.find(e) == O.end())
            {
                O[e] = 1;
            }
            else 
            {
                O[e]++;
            }
        }

        std::set<int> S;

        for (auto [k, v] : O)
        {
            S.insert(v);
        }
    

        return S.size() == O.size();
    }
};