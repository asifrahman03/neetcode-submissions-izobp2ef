class Solution {
    public int[] twoSum(int[] numbers, int target) {
        HashMap<Integer, Integer> hM = new HashMap<>();
        int[] res = new int[2];
        for(int i=0; i<numbers.length; i++){
            int diff = target-numbers[i];
            if(!hM.containsKey(diff)){
                hM.put(numbers[i], i);
            }else{
                res[0] = hM.get(diff)+1;
                res[1] = i+1;
            }
        }
        return res;

    }
}
