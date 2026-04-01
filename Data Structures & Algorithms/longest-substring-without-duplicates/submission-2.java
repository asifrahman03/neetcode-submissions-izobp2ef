class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length() == 0) return 0;
        if(s.length() == 1) return 1;

        int l= 0;
        int r = 0;
        int mLen = 0;
        Set<Character> set = new HashSet<>();
        for(;r<s.length(); r++){
            while(set.contains(s.charAt(r))){
                set.remove(s.charAt(l));
                l++;
            }
            set.add(s.charAt(r));
            String substring = s.substring(l, r+1);
            mLen = Math.max(substring.length(), mLen);
        }
        return mLen;
    }
}
