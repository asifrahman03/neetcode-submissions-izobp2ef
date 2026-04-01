class Solution {
    public boolean isPalindrome(String s) {
        String low = s.toLowerCase();
        String trim = low.trim();
        StringBuilder sB = new StringBuilder();
        for(char c : trim.toCharArray()){
            if(Character.isLetterOrDigit(c)){
                sB.append(c);
            }
        }
        String check = sB.toString();
        int left = 0;
        int right = check.length()-1;

        while(left < right){
            if(check.charAt(left) != check.charAt(right)){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
