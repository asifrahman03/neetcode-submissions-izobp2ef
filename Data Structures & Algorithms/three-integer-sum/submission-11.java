class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();

        Arrays.sort(nums);

        for(int i=0; i<nums.length; i++){
            if(nums[i] > 0) break;
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            int l = i+1;
            int r = nums.length-1;

            while (l < r){
                int check = nums[i] + nums[l] + nums[r];

                if(check > 0){
                    r--;
                }
                else if(check < 0){
                    l++;
                }
                else{
                    List<Integer> yes = new ArrayList<>();
                    yes.add(nums[i]);
                    yes.add(nums[l]);
                    yes.add(nums[r]);
                    res.add(yes);
                    l++;
                    while(l < r && nums[l] == nums[l-1]){
                        l++;
                    }
                }
            }
        }
        return res;


    }
}
