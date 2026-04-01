class Solution {
    public boolean isValid(String s) {
        Stack<Character> paren = new Stack<>();
        for(char c : s.toCharArray()){
            if(c == '[' || c == '(' || c=='{'){
                paren.push(c);
            }
            else if((c == ')' || c==']' || c=='}') && paren.empty()){
                return false;
            }
            else if(c==')' && paren.peek() != '(' || c==']' && paren.peek() != '[' || c=='}' && paren.peek() != '{'){
                return false;
            }
            else if(c==')' && paren.peek() == '('){
                paren.pop();
            }
            else if(c==']' && paren.peek() == '['){
                paren.pop();
            }
            else if(c=='}' && paren.peek() == '{'){
                paren.pop();
            }
        }
        return paren.empty();
    }
}
