class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length - 1;
        int[] res = new int[2];
        while(l<r){
            int total = numbers[l] + numbers[r];
            if(total < target){
                l++;
            }
            else if(total > target){
                r--;
            }else{
                res[0] = l+1;
                res[1] = r+1;
                return res;
            }
        }
        return res;
    }
}
