class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<Integer>();

        for(int i = 0; i<nums.length; i++){
            set.add(nums[i]);
        }
        int res = 0;

        for(int num : set){
            if(!set.contains(num-1)){
                int len = 1;
                while(set.contains(num + len)){
                    len++;
                }
                res = Math.max(res, len);
            }
        }
        return res;
    }
}
