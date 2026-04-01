class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hM = new HashMap<>();
        int[] ans = new int[2];
        for(int i=0; i<nums.length; i++){
            int offset = target - nums[i];
            if(hM.containsKey(offset)){
                ans[0] = hM.get(offset);
                ans[1] = i;
                return ans;
            }
            hM.put(nums[i], i);
        }
        return ans;
    }
}
