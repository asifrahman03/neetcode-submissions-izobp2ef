class Solution {
    public int maxArea(int[] heights) {
        int l = 0, r=heights.length-1;
        int maxA = 0;
        while(l<r){
            int minH = Math.min(heights[l], heights[r]);
            int area = minH * (r-l);
            maxA = Math.max(maxA, area);
            if(heights[l] < heights[r]){
                l++;
            }else{
                r--;
            }
        }
        return maxA;
    }
}
