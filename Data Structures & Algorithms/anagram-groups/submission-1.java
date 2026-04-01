class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> hM = new HashMap<>();
        for(int i=0; i<strs.length; i++){
            int[] count = new int[26];
            for(int j=0; j<strs[i].length(); j++){
                count[strs[i].charAt(j)-'a']++;
            }
            String k = Arrays.toString(count);
            if(!hM.containsKey(k)){
                hM.put(k, new ArrayList<String>());
            }
            hM.get(k).add(strs[i]);
        }
        List<List<String>> res = new ArrayList<>();
        for(List<String> s : hM.values()){
            res.add(s);
        }
        return res;
    }
}
