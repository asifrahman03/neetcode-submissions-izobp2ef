class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int i=0; i<nums.length; i++){
            set.add(nums[i]);
        }
        int maxCount = 0;
        for(int num : set){
            if(!set.contains(num-1)){
                int newList = 1;
                while(set.contains(num + newList)){
                    newList++;
                }
                maxCount = Math.max(maxCount, newList);
            }
        }
        return maxCount;
    }
}
