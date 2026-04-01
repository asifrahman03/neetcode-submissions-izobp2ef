class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        HashMap<Character, Integer> hM = new HashMap<>();
        char[] sArr = s.toCharArray();
        for(int i=0; i<sArr.length; i++){
            if(!hM.containsKey(sArr[i])){
                hM.put(sArr[i], 1);
            }
            else{
                hM.put(sArr[i], hM.get(sArr[i])+1);
            }
        }
        char[] tArr = t.toCharArray();
        for(int j=0; j<tArr.length; j++){
            if(!hM.containsKey(tArr[j])){
                return false;
            }
            else{
                hM.put(tArr[j], hM.get(tArr[j])-1);
            }
        }
        for(Integer k : hM.values()){
            if(k != 0){
                return false;
            }
        }
        return true;
    }
}
