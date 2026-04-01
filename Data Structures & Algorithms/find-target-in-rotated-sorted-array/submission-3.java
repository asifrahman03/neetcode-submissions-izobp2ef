class Solution {
    public int search(int[] nums, int target) {
        int low= 0;
        int high= nums.length-1;

        while(low <= high){
            if(nums[low] <= nums[high]){
                int mid2 = low + (high-low)/2;

                if(nums[mid2] == target) return mid2;

                if(nums[mid2] < target){
                    low = mid2+1;
                }else{
                    high = mid2-1;
                }
                continue;
            }
            int mid = low + (high-low)/2;

            if(nums[mid] == target){
                return mid;
            }
            if(nums[low] == target) return low;
            if(nums[mid] >= nums[low]){
                low = mid+1;
            }
            else {
                if(nums[high] == target) return high;
                high = mid -1;
            }
        }
        return -1;
    }
}
