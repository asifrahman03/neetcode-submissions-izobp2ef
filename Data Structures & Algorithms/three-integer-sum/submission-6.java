class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        // int r = nums.length-1;
        Arrays.sort(nums);

        for(int i=0; i<nums.length; i++){
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            if(nums[i] > 0){
                break;
            }
            int r = nums.length-1;
            int l = i+1;
            while(l<r){
                int total = nums[i] + nums[l] + nums[r];
                if(total == 0){
                    List<Integer> pairM = new ArrayList<>();
                    pairM.add(nums[i]);
                    pairM.add(nums[l]);
                    pairM.add(nums[r]);
                    res.add(pairM);
                    l++;
                    r--;
                    while(nums[l] == nums[l-1] && l<r){
                        l++;
                    }
                }
                else if(total > 0){
                    r--;
                }
                else{
                    l++;
                } 
            }
        }
        return res;
    }
}
