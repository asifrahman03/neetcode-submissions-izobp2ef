class Solution {
    public int findMin(int[] nums) {
        // if(nums.length == 1){
        //     return nums[0];
        // }
        int low = 0;
        int high = nums.length-1;
        int res = Integer.MAX_VALUE;

        while(low <= high){
            if(nums[low] < nums[high]) {
                res = Math.min(res, nums[low]);
                break;
            }

            int mid = low + (high-low)/2;

            if(nums[mid] < res) res = nums[mid];

            if(nums[mid] >= nums[low]){
                low = mid + 1;
            }
            else{
                high = mid-1;
            }
        }

        return res;

    }
}
