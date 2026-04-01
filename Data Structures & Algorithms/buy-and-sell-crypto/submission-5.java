class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length == 1){
            return 0;
        }
        int l = 0;
        int currComp = 0;
        int r = 1;
        while(r < prices.length){
            int comp = prices[r] - prices[l];
            if(comp < 0){
                l = r;
            }
            else if(comp > currComp){
                currComp = comp;
            }
            r++;
        }
        return currComp;
    }
}
