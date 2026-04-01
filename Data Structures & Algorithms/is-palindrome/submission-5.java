class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length()-1;
        String j = s.toLowerCase();
        while(l<r){
            while(l<r && !Character.isLetterOrDigit(j.charAt(l))){
                l++;
            }
            while(l<r && !Character.isLetterOrDigit(j.charAt(r))){
                r--;
            }
            if(j.charAt(l) != j.charAt(r)){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
