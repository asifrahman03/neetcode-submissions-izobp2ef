class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for(int i : nums){
            set.add(i);
        }
        int res = 0;

        for(int i : set){
            if(!set.contains(i-1)){
                int len = 1;
                while(set.contains(i+len)){
                    len++;
                }
                res = Math.max(res, len);
            }
        }
        return res;
    }
}
