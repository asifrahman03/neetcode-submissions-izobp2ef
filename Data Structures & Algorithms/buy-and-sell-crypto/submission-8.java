class Solution {
    public int maxProfit(int[] prices) {
        // if(prices.length < 2){
        //     return 0;
        // }
        int l = 0;
        int res = 0;
        for(int r = 1; r<prices.length; r++){
            if(prices[r] < prices[l]) l = r;
            else {
                int profit = prices[r] - prices[l];
                res = Math.max(res, profit);
            }
        }
        return res;
    }
}
