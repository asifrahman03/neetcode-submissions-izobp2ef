class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        HashMap<String, List<String>> hM = new HashMap<>();

        int[] count = new int[26];
        for(int i=0; i<strs.length; i++){
            for(char c : strs[i].toCharArray()){
                count[c-'a']++;
            }
            StringBuilder reconstructedString = new StringBuilder();
            for (int j = 0; j < 26; j++) {
                while (count[j] > 0) {
                    reconstructedString.append((char) ('a' + j));
                    count[j]--;
                }
            }
            String keyString = reconstructedString.toString();
            if(!hM.containsKey(keyString)){
                hM.put(keyString, new ArrayList<>());
                hM.get(keyString).add(strs[i]);
            }else{
                hM.get(keyString).add(strs[i]);
            }
        }

        for(List<String> set : hM.values()){
            res.add(set);
        }
        return res;
    }
}
