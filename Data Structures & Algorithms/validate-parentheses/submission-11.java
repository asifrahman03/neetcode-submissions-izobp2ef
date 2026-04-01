class Solution {
    public boolean isValid(String s) {
        if(s.length() <= 1) return false;
        Stack<Character> stack = new Stack<>();

        for(int i = 0; i<s.length(); i++){
            char c = s.charAt(i);

            if(c == '(' || c=='[' || c=='{'){
                stack.push(c);
            }

            if((c == ')' || c==']' || c=='}') && stack.empty()){
                return false;
            }

            if((c == ')' && stack.peek() != '(') || (c == ']' && stack.peek() != '[') || (c == '}' && stack.peek() != '{')){
                return false;
            }

            if(!stack.empty() && stack.peek() == '(' && c == ')'){
                stack.pop();
            }
            else if(!stack.empty() && stack.peek() == '[' && c == ']'){
                stack.pop();
            }
            else if(!stack.empty() && stack.peek() == '{' && c == '}'){
                stack.pop();
            }
        }
        return stack.empty();
    }
}
