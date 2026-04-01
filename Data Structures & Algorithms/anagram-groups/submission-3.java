class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        HashMap<String, List<String>> hM = new HashMap<>();
        for(String s : strs){
            String keyS = keyBuilder(s);
            if(!hM.containsKey(keyS)){
                hM.put(keyS, new ArrayList<>());
                hM.get(keyS).add(s);
            }else{
                hM.get(keyS).add(s);
            }
        }
        for(List<String> lS : hM.values()){
            res.add(lS);
        }
        return res;
    }

    private String keyBuilder(String st){
        StringBuilder sB = new StringBuilder();
        char[] stArr = st.toCharArray();
        Arrays.sort(stArr);
        for(char c : stArr){
            sB.append(c);
        }
        return sB.toString();
    }
}
