class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0;
        HashSet<Character> hS = new HashSet<>();
        int maxT = 0;
        for(int i=0; i<s.length(); i++){
            while(hS.contains(s.charAt(i))){
                hS.remove(s.charAt(l));
                l++;
            }
            hS.add(s.charAt(i));
            maxT = Math.max(maxT, i-l+1);
        }
        return maxT;
    }
}
