class Solution {
    public int longestConsecutive(int[] nums) {
        int res = 0;
        HashSet<Integer> hS = new HashSet<>();
        for(int j=0; j<nums.length; j++){
            hS.add(nums[j]);
        }
        for(int i : hS){
            if(!hS.contains(i-1)){
                int currCount = 0;
                while(hS.contains(i+currCount)){
                    currCount++;
                }
                res = Math.max(res, currCount);
            }
            
        }
        return res;
    }
}
