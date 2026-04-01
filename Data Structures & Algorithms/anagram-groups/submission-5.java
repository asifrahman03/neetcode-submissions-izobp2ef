class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();

        for(String str : strs){
            int[] freq = new int[26];
            for(int i=0; i<str.length(); i++){
                freq[str.charAt(i) - 'a']++;
            }
            String check = Arrays.toString(freq);

            if(!map.containsKey(check)){
                List<String> newL = new ArrayList<>();
                newL.add(str);
                map.put(check, newL);
            }else{
                map.get(check).add(str);
            }
        }
        for(Map.Entry<String, List<String>> entry : map.entrySet()){
            res.add(entry.getValue());
        }
        return res;
    }
}
