class Solution {
    public int maxArea(int[] heights) {
        int l = 0;
        int r = heights.length-1;
        int currM = 0;
        while(l<r){
            int sumT = Math.min(heights[l], heights[r]) * (r-l);
            currM = Math.max(currM, sumT);
            if(heights[l] < heights[r]){
                l++;
            }else{
                r--;
            }
        }
        
        return currM;
    }
}
