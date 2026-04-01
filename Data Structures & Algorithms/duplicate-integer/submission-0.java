class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> hS = new HashSet<>();
        for(int i : nums){
            if(!hS.add(i)){
                return true;
            }
        }
        return false;
    }
}
