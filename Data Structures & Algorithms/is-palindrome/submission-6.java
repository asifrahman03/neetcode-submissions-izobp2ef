class Solution {
    public boolean isPalindrome(String s) {
        String lower = s.toLowerCase();
        StringBuilder sB = new StringBuilder();
        char[]sArr = lower.toCharArray();
        for(char c : sArr){
            if(Character.isLetterOrDigit(c)){
                sB.append(c);
            }
        }
        String fixed= sB.toString();
        int l = 0;
        int r = fixed.length()-1;
        while(l<r){
            if(fixed.charAt(l) != fixed.charAt(r)){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
