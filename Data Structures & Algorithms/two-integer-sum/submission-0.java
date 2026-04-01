class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        HashMap<Integer, Integer> hM = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            int remainder = target - nums[i];
            if(!hM.containsKey(remainder)){
                hM.put(nums[i], i);
            }
            else{
                res[0] = hM.get(remainder);
                res[1] = i;
                return res;
            }
        }
        return res;
    }
}
