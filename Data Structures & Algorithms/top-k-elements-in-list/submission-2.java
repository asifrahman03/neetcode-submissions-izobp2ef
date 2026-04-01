class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] res = new int[k];
        Map<Integer, Integer> hM = new HashMap<>();
        List<Integer>[] freq = new ArrayList[nums.length+1];
        for(int i=1; i<freq.length; i++){
            freq[i] = new ArrayList<>();
        }
        for(int i : nums){
            hM.put(i, hM.getOrDefault(i, 0)+1);
        }
        for(Map.Entry<Integer, Integer> set : hM.entrySet()){
            freq[set.getValue()].add(set.getKey());
        }
        int index = 0;
        for(int i=freq.length-1; i>0 && index < k; i--){
            if(freq[i].size()>0){
                for(int j=0; j<freq[i].size(); j++){
                    res[index] = freq[i].get(j);
                    index++;
                }
            }
        }
        return res;
    }
}
