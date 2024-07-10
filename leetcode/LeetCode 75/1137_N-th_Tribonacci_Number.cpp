class Solution {
public:
    int tribonacci(int n) {
        int t0=0, t1=1, t2=1;
        int tn;
        if(n == 0) return t0;
        if(n == 1) return t1;
        if(n == 2) return t2;

        
        for(int i = 0; i<n-2; i++){
            tn = t1+t2+t0;
            t0 = t1;
            t1 = t2;
            t2 = tn;
        }
        return tn;

    }
};