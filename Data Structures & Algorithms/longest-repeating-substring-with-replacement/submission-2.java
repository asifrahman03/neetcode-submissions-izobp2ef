class Solution {
    public int characterReplacement(String s, int k) {
        int l = 0;
        HashMap<Character, Integer> hM = new HashMap<>();
        int res = 0;
        int windowLen = 0;

        for(int r = 0; r<s.length(); r++){
            hM.put(s.charAt(r), hM.getOrDefault(s.charAt(r), 0)+1);
            windowLen = r-l+1;
            int mostFreq = 0;
            for(Integer p : hM.values()){
                mostFreq = Math.max(mostFreq, p);
            }
            int check = windowLen - mostFreq;
            if(check <= k){
                res = windowLen;
            }else{
                l++;
                char c = s.charAt(l-1);
                hM.put(c, hM.get(c)-1);
            }
        }

        return res;
    }
}
