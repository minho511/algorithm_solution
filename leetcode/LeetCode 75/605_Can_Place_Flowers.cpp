class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int s = flowerbed.size();
        if(n==0) return 1;
        for(int i = 0; i<s; i++){
            if(flowerbed[i] == 1) continue;
            if((i==0||flowerbed[i-1] == 0) && (i==s-1||flowerbed[i+1]==0 )){
                flowerbed[i] = 1;
                n--;
                if(n==0) return 1;
            }
        }
        return 0;
    }
};