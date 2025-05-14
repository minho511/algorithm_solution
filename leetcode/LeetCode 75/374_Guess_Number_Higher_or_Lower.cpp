/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        long long s = 1, e = n;
        long long a;
        long long k;
        while(s<e){
            a = (s+e)/2;
            k = guess(a);
            if(k == 0){
                return a;
            }
            else if(k==1){
                s = a+1;
            }else{
                e = a-1;
            }
        }
        return s;
    }
};