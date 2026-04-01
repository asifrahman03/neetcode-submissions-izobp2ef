class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        int[] cArr = new int[26];

        for(char c : s.toCharArray()){
            cArr[c-'a']++;
        }

        for(char d : t.toCharArray()){
            cArr[d-'a']--;
        }

        for(int i=0; i<cArr.length; i++){
            if(cArr[i] != 0){
                return false;
            }
        }
        return true;
    }
}
