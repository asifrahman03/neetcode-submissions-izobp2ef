class Solution {
    public int maxProfit(int[] prices) {
        int sell = 1;
        int buy = 0;
        int res = 0;

        while(sell < prices.length){
            int sum = prices[sell] - prices[buy];

            res = Math.max(res, sum);

            if(prices[sell] < prices[buy]){
                buy = sell;
            }
            sell++;

        }

        return res;
    }
}
