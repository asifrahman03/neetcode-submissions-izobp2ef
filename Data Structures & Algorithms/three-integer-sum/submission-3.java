class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        for(int i=0; i<nums.length; i++){
            if(nums[i] > 0) break;
            if(i > 0 && nums[i] == nums[i-1])continue;
            int l = i+1;
            int r = nums.length-1;
            while(l<r){
                int total = nums[i]+nums[l]+nums[r];
                if(total < 0){
                    l++;
                }
                else if(total > 0){
                    r--;
                }else{
                    List<Integer> aMatch = new ArrayList<>();
                    aMatch.add(nums[i]);
                    aMatch.add(nums[l]);
                    aMatch.add(nums[r]);
                    res.add(aMatch);
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
