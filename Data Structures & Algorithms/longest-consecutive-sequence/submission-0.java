class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> hS = new HashSet<>();
        int maxCount = 0;
        Arrays.sort(nums);
        for(int i=0; i<nums.length; i++){
            hS.add(nums[i]);
        }
        for(int j : hS){
            if(!hS.contains(j-1)){
                int currCount = 1;
                while(hS.contains(j+currCount)){
                    currCount++;
                }
                maxCount = Math.max(currCount, maxCount);
            }
        }
        return maxCount;
    }
}
