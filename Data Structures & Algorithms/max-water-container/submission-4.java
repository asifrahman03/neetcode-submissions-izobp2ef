class Solution {
    public int maxArea(int[] heights) {
        int l = 0;
        int r = heights.length-1;
        int res = 0;

        while (l < r){
            int length = r-l;

            int currH = Math.min(heights[l], heights[r]);

            int currRes= length * currH;
            res= Math.max(res, currRes);
            if(heights[l] < heights[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return res;
    }
}
