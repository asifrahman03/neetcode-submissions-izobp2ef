class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] res = new int[k];
        HashMap<Integer, Integer> hM = new HashMap<>();

        for(int i=0; i<nums.length; i++){
            hM.put(nums[i], hM.getOrDefault(nums[i], 0)+1);
        }

        List<Integer>[] count = new ArrayList[nums.length+1];
        for(int o=0; o<count.length; o++){
            count[o] = new ArrayList<>();
        }
        for(int h : hM.keySet()){
            int v = hM.get(h);
            count[v].add(h);
        }

        int check = 0;
        for(int l=count.length-1; l>=0 && check<=k; l--){
            for(int p: count[l]){
                res[check] = p;
                check++;
                if(check == k){
                    return res;
                }
            }
        }
        return res;
    }
}
