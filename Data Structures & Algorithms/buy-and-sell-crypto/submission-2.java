class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int buyDay = 0;
        for(int i=0; i<prices.length-1; i++){
            for(int j=i+1; j<prices.length; j++){
                int difference = prices[j] - prices[i];
                if(difference > profit){
                    profit = difference;
                }
            }
        }
        return profit;
    }
}
