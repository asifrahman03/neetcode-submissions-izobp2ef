class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] res= new int[k];
        HashMap<Integer, Integer> hM = new HashMap<>();

        for(int i=0; i<nums.length; i++){
            hM.put(nums[i], hM.getOrDefault(nums[i], 0)+1);
        }

        List<Integer>[] check = new ArrayList[nums.length+1];
        for(int i=0; i<check.length; i++){
            check[i] = new ArrayList<>();
        }
        for(int i : hM.keySet()){
            int val = hM.get(i);
            check[val].add(i);
        }
        int index = 0;
        for(int i=check.length-1; i>0 && index < k; i--){
            while(check[i].size() > 0){
                int num = check[i].remove(check[i].size()-1);
                res[index] = num;
                index++;
            }
        }
        return res;
    }
}
