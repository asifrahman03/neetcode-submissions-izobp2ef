class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hM = new HashMap<>();
        int[] res = new int[2];

        for(int i=0; i<nums.length; i++){
            int complement = target - nums[i];
            if(!hM.containsKey(complement)){
                hM.put(nums[i], i);
            }else{
                res[0] = hM.get(complement);
                res[1] = i;
                return res;
            }
        }
        return res;
    }
}
