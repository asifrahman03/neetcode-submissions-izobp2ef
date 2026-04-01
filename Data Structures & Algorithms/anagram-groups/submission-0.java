class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if(strs.length < 1 || strs == null){
            return new ArrayList<>();
        }
        HashMap<String, List<String>> hM = new HashMap<>();
        for(String str: strs){
            String sorted = getFreqString(str);

            if(hM.containsKey(sorted)){
                hM.get(sorted).add(str);
            }else{
                ArrayList<String> newList = new ArrayList<String>();
                newList.add(str);
                hM.put(sorted, newList);
            }
        }
        return new ArrayList<>(hM.values());
    }
    private String getFreqString(String str){
        int[] count = new int[26];

        for(Character c : str.toCharArray()){
            count[c-'a']++;
        }

        StringBuilder construct = new StringBuilder("");
        char c= 'a';
        for(int i : count){
            construct.append(c);
            construct.append(i);
            c++;
        }
        return construct.toString();
    }
}
