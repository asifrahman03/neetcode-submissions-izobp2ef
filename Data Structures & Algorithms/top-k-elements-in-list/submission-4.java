class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] res = new int[k];
        List<Integer>[] freq = new ArrayList[nums.length+1];

        // Initialize each ArrayList in the array
        for(int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        Map<Integer, Integer> map = new HashMap<>();

        for(int i=0; i<nums.length; i++){
            map.put(nums[i], map.getOrDefault(nums[i], 0)+1);
        }

        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            freq[entry.getValue()].add(entry.getKey());
        }

        int check = 0;
        for(int i=freq.length-1; i>0 && check < k; i--){
            for(int j=0; j<freq[i].size(); j++){
                res[check] = freq[i].get(j);
                check++;
                if(check == k){
                    return res;
                }
            } 
        }
        return res;
    }
}
