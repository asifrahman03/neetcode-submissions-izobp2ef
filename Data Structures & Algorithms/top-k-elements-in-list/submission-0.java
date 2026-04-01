class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> countMap = new HashMap<>();
        ArrayList<Integer>[] freqArr = new ArrayList[nums.length+1];

        for(int j : nums){
            countMap.put(j, countMap.getOrDefault(j, 0)+1);
        }

        for(int i=0; i<freqArr.length; i++){
            freqArr[i] = new ArrayList<>();
        }

        for(int u : countMap.keySet()){
            int freq = countMap.get(u);
            freqArr[freq].add(u);
        }

        int[] res = new int[k];
        int check = 0;
        for(int l=freqArr.length-1; l>0 && check < k; l--){
            for(int p : freqArr[l]){
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
