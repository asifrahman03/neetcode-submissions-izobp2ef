class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);

        for(int i=0; i<nums.length; i++){
            // if(nums[i] > 0) break;
            if(i > 0 && nums[i]==nums[i-1]){
                continue;
            }
            int l = i+1;
            int r = nums.length-1;
            while(l<r){
                int total = nums[l] + nums[i] + nums[r];
                if(total < 0){
                    l++;
                }else if(total > 0){
                    r--;
                }else{
                    List<Integer> pair= new ArrayList<>();
                    pair.add(nums[l]);
                    pair.add(nums[i]);
                    pair.add(nums[r]);
                    res.add(pair);
                    l++;
                    r--;
                    while(nums[l] == nums[l-1] && l<r){
                        l++;
                    }
                }
            }
        }
        return res;
    }
}
