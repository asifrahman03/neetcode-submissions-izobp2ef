class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        HashMap<String, List<String>> hM = new HashMap<>();

        for(String str: strs){
            int[] count = new int[26];
            for(char c : str.toCharArray()){
                count[c-'a']++;
            }
            String some = Arrays.toString(count);
            if(!hM.containsKey(some)){
                hM.put(some, new ArrayList<>());
            }
            hM.get(some).add(str);
        }
        for(List<String> iter : hM.values()){
            res.add(iter);
        }
        return res;
    }
}
