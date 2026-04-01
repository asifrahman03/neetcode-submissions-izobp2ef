class Solution {
    public int maxArea(int[] heights) {
        int maxSize = 0;
        int l = 0;
        int r = heights.length-1;

        while(l<r){
            int currMinHeight = Math.min(heights[l], heights[r]);
            int currLen = r-l;
            int currSize = currMinHeight*currLen;
            // int currSize = heights[l] * heights[r];
            maxSize = Math.max(maxSize, currSize);
            if(currMinHeight == heights[l]){
                l++;
            }else{
                r--;
            }
        }
        return maxSize;

    }
}
