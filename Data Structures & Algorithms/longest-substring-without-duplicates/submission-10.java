class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0;
        int l = 0;
        int r = 0;
        Set<Character> set = new HashSet<>();

        while(r < s.length()){
            char c = s.charAt(r);
            while(set.contains(c)){
                char lChar= s.charAt(l);
                set.remove(lChar);
                l++;
            }
            set.add(c);
            res = Math.max(res, r-l+1);
            r++;
        }
        return res;
    }
}
