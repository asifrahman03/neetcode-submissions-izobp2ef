class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        List<Integer> res = new ArrayList<>();
        /*
        Create left pointer at 0, right as iterator = k-1
        Create temp pointer to iterate inside window to get max
        */
        int left = 0;
        for(int right = k-1; right<nums.length; right++){
            int currN = Integer.MIN_VALUE;
            for(int j = left; j<=right; j++){
                currN = Math.max(currN, nums[j]);
            }
            res.add(currN);
            left++;
        }
        int len = res.size();
        int[] trueRes = new int[len];
        for(int i=0; i<res.size(); i++){
            trueRes[i] = res.get(i);
        }
        return trueRes;

    }
}
