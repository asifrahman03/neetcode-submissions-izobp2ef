class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int right = 0;
        for(int i=0; i<piles.length; i++){
            right = Math.max(right, piles[i]);
        }
        int left = 0;
        int res = right;

        while(left <= right){
            int k = (left+right)/2;
            int hours = 0;
            for(int p=0; p<piles.length; p++){
                hours += Math.ceil((double)piles[p]/k);
            }
            if(hours <= h){
                res= Math.min(res, k);
                right = k-1;
            }else{
                left = k+1;
            }
        }
        return res;
    }
}
